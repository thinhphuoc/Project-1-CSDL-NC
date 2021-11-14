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
    public partial class Form_XemDSHD : Form
    {
        public Form_XemDSHD()
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

        private void Load_HoaDon()
        {

        }

        private void Form_XemDSHD_Load_1(object sender, EventArgs e)
        {
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
