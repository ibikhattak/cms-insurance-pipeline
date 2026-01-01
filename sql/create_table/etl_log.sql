USE CMS_PDS_DATA;
GO

CREATE TABLE etl_log (
    run_id INT IDENTITY(1,1) PRIMARY KEY,
    file_name VARCHAR(255),
    rows_loaded INT,
    rows_failed INT,
    started_at DATETIME,
    completed_at DATETIME,
    status VARCHAR(20),
    message VARCHAR(MAX)
);
GO