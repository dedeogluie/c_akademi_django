const { Pool } = require("pg");

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "todoapp",
  password: "kendişifrenizigirin",
  port: 5432,
});

const creatTodoTable = async () => {
  try {
    const createTableQuery = `
        CREATE TABLE IF NOT EXISTS todo(
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            description TEXT NOT NULL,
            completed BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        ) `;

    const client = await pool.connect();
    await client.query(createTableQuery);
    client.release();

    console.log("Todo tablosu başarıyla oluşturuldu");
  } catch (error) {
    console.log("Tablo oluşturulmadı", error);
  }
};

module.exports = {
  pool,
  creatTodoTable,
};
