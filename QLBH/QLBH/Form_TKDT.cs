using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace QLBH
{
    public partial class Form_TKDT : Form
    {
        public Form_TKDT()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();
            Form1 formTHD = new Form1();
            formTHD.ShowDialog();
            this.Close();
        }

        private void Form_TKDT_Load(object sender, EventArgs e)
        {

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
        SqlConnection cnn = new SqlConnection(@"Data Source=LAPTOP-FGLN4TT3\SQLEXPRESS;Initial Catalog = QLBH;Integrated Security = True");
        private void button2_Click(object sender, EventArgs e)
        {
            String month = comboBox1.Text;
            var year = textBox1.Text.Trim();

            cnn.Open();
            string sql = "select * from HoaDon where NgayLap between '" + year + "-"+ month+ "-01 00:00:00' AND '" + year + "-" + month + "-31 23:59:59'";  // lay het du lieu trong bang sinh vien
            SqlCommand com = new SqlCommand(sql, cnn); //bat dau truy van
            com.CommandType = CommandType.Text;
            SqlDataAdapter da = new SqlDataAdapter(com); //chuyen du lieu ve
            DataTable dt = new DataTable(); //tạo một kho ảo để lưu trữ dữ liệu
            da.Fill(dt);  // đổ dữ liệu vào kho
            cnn.Close();  // đóng kết nối
            dataGridView1.DataSource = dt; //đổ dữ liệu vào datagridview

            //Allign các cell dữ liệu trên datagridview
            dataGridView1.Columns[0].HeaderCell.Style.Alignment = DataGridViewContentAlignment.MiddleLeft;
            dataGridView1.Columns[0].Width = 130;
            dataGridView1.Columns[0].DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight;
            dataGridView1.Columns[0].HeaderText = "Mã hóa đơn";

            dataGridView1.Columns[1].HeaderCell.Style.Alignment = DataGridViewContentAlignment.MiddleLeft;
            dataGridView1.Columns[1].Width = 150;
            dataGridView1.Columns[1].DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight;
            dataGridView1.Columns[1].HeaderText = "Mã khách hàng";

            dataGridView1.Columns[2].HeaderCell.Style.Alignment = DataGridViewContentAlignment.MiddleLeft;
            dataGridView1.Columns[2].AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
            dataGridView1.Columns[2].DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight;
            dataGridView1.Columns[2].HeaderText = "Ngày lặp";

            dataGridView1.Columns[3].HeaderCell.Style.Alignment = DataGridViewContentAlignment.MiddleLeft;
            dataGridView1.Columns[3].Width = 200;
            dataGridView1.Columns[3].DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleRight;
            dataGridView1.Columns[3].HeaderText = "Thành tiền";
        }
    }
}
