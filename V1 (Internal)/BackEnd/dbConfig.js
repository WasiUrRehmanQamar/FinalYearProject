const sql = require('mssql/msnodesqlv8')

var config = {
  database: 'FYP',
  server: 'DESKTOP-8M72HBG\\SQLEXPRESS',
  driver: 'msnodesqlv8',
  options: {
      trustedConnection: true
  }
};

sql.connect(config, err => {
  if (err) console.log(err);
  else console.log("Connected to the database!");
});

module.exports = { config }