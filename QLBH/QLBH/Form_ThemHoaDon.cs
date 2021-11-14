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
    public partial class Form_ThemHoaDon : Form
    {
        public Form_ThemHoaDon()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Hide();
            Form1 formTHD = new Form1();
            formTHD.ShowDialog();
            this.Close();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void Form_ThemHoaDon_Load(object sender, EventArgs e)
        {

        }

        SqlConnection cnn = new SqlConnection(@"Data Source=LAPTOP-FGLN4TT3\SQLEXPRESS;Initial Catalog = QLBH;Integrated Security = True");
        private void button1_Click(object sender, EventArgs e)
        {

            var MaHD = textBox1.Text.Trim();
            var MaKH = textBox2.Text.Trim();
            var NgayLap = textBox3.Text.Trim();
            var ThanhTien = int.Parse(textBox4.Text);

            if (string.IsNullOrEmpty(MaHD))
            {
                MessageBox.Show("Vui lòng nhập mã hóa đơn", "Ràng buộc dữ liệu", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;//dừng chương trình ngang đây
            }

            if (string.IsNullOrEmpty(MaKH))
            {
                MessageBox.Show("Vui lòng nhập mã khách hàng", "Ràng buộc dữ liệu", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;//dừng chương trình ngang đây
            }
            if (ThanhTien < 0)
            {
                MessageBox.Show("Thành tiền không hợp lệ", "Ràng buộc dữ liệu", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;//dừng chương trình ngang đây
            }

            SqlCommand cmd = new SqlCommand();
            cmd.CommandType = CommandType.StoredProcedure;
            cmd.CommandText = "themHoaDon"; // Store procediure name
            cmd.Parameters.Add("@MaHD", SqlDbType.VarChar).Value = MaHD;
            cmd.Parameters.Add("@MaKH", SqlDbType.VarChar).Value = MaKH;
            cmd.Parameters.Add("@NgayLap", SqlDbType.VarChar).Value = NgayLap;
            cmd.Parameters.Add("@ThanhTien", SqlDbType.VarChar).Value = ThanhTien;

            cmd.Connection = cnn;
            try
            {
                cnn.Open();
                try
                {
                    var rs = cmd.ExecuteNonQuery();
                    if (rs == 1)
                    {
                        MessageBox.Show("Thêm mới thành công!", "Success !", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                    else
                    {
                        MessageBox.Show("Thêm mới không thành công!", "Failed !", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                }
                catch (SqlException ex)
                {
                    MessageBox.Show(ex.Message);
                    cnn.Close();
                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
            finally
            {
                cmd.Dispose();
                cnn = null;
                cmd = null;
            }
        }
    }
}
