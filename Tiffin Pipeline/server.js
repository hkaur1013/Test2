const express = require('express');
const mysql = require('mysql');
const ejs = require('ejs');

const app = express();
const port = 3000;

// Create a MySQL connection
const db = mysql.createConnection({
   // host: 'your_mysql_host',
  // host: '70.48.31.76',
 // host: '127.0.0.1',
host: '192.168.2.15',
    user: 'root',
    password: 'Gmsshn!43',
    database: 'sql9602732'
});

// Connect to the database
db.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL database');
});

// Set EJS as the view engine
app.set('view engine', 'ejs');


// Define a route to fetch data from the 'your_table_name' table
app.get('/', (req, res) => {
    const sql = 'select Serial_No ,Customer_Name ,Customer_Address ,Customer_Phone_Number  from tiffin_service ts where is_active_master =1';
    db.query(sql, (err, result) => {
        if (err) {
            console.error('Error executing query:', err);
            res.status(500).send('Internal Server Error');
            return;
        }

        // Render the data in an HTML page using EJS
        res.render('index', { data: result });
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
