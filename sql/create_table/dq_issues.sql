USE CMS_PDS_DATA;
GO

CREATE TABLE dq_issues (
    issue_id INT IDENTITY(1,1) PRIMARY KEY,
    provider_id VARCHAR(20),
    issue_type VARCHAR(255),
    issue_details VARCHAR(MAX),
    row_data VARCHAR(MAX),
    detected_at DATETIME DEFAULT GETDATE()
);
GO