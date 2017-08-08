using System;
using System.Collections.Generic;
using System.IO;
using System.Data;
using System.Data.OleDb;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Excel = Microsoft.Office.Interop.Excel;
using Outlook = Microsoft.Office.Interop.Outlook;


namespace table_binding
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            
        }
        private void load_table()
        {
            String name = "Sheet1";
            String constr = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" +
                            "Jobs.xlsx" +
                            ";Extended Properties='Excel 12.0 XML;HDR=YES;';";

            OleDbConnection con = new OleDbConnection(constr);
            OleDbCommand oconn = new OleDbCommand("Select * From [" + name + "$]", con);
            con.Open();

            OleDbDataAdapter sda = new OleDbDataAdapter(oconn);
            DataTable data = new DataTable();
            sda.Fill(data);

            dataGrid1.ItemsSource = data.DefaultView;
            con.Close();

        }
        private bool save_new_data()
        {
            String name = "Sheet1";
            String constr = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" +
                            "Jobs.xlsx" +
                            ";Extended Properties='Excel 12.0 XML;HDR=YES;';";
            OleDbCommand oconn = new OleDbCommand();

            try
            { 
            OleDbConnection con = new OleDbConnection(constr);
            jobSummary.SelectAll();
                con.Open();
                            oconn.Connection = con;
                oconn.CommandText = "Insert into [" + name + "$] ([JobTitle],[CompanyName],[URL],[Description],[Applied_on],[Status],[Note]) values (" +
                "\""+jobTitle.Text + "\"," +
                "\""+companyName.Text + "\"," +
                "\""+postURL.Text + "\"," +
                "\"" + jobSummary.Selection.Text.Trim() + "\"," +
                "\"" + Applied_On.SelectedDate.ToString() + "\"," +
                "\"" + status.Text + "\"," +
                "\"" + comments.Text + "\");";
                
                oconn.ExecuteNonQuery();
                con.Close();

                return true;
            }
            catch(OleDbException e)
            {
                MessageBox.Show(e.ToString()+ oconn.CommandText.ToString());
                return false; 
            }



        }
        private void Load_Click(object sender, RoutedEventArgs e)
        {
            if (reaminder_checkBox.IsChecked.Value)
            {
                Outlook.Application outlookApp = new Outlook.Application();

                Outlook.AppointmentItem appt = outlookApp.CreateItem(Outlook.OlItemType.olAppointmentItem);
                appt.Subject = "Follow up for"+ jobTitle.Text+ " post "+ companyName.Text;
                appt.Location = "NA";
                appt.Body = "Follow up with the HR/Website for the Status ";
                appt.Sensitivity = Outlook.OlSensitivity.olPrivate;
                appt.Start = DateTime.Parse(remainder_date.SelectedDate.ToString());
                appt.End = DateTime.Parse(remainder_date.SelectedDate.ToString().Replace("00:00","10:00"));
                appt.ReminderSet = true;
                appt.ReminderMinutesBeforeStart = 0;
                appt.Save();
            } 
            if (save_new_data())
                load_table();
            else
                MessageBox.Show("Data Invalid:Please check"); 


        }

        private void dataGrid1_Loaded(object sender, RoutedEventArgs e)
        {
            if (File.Exists("Jobs.xlsx"))
                load_table();
            else
                MessageBox.Show("No file found");
        }
    }
}
