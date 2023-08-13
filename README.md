# **File Manager**

This project refers to a system that receives files, processes their data and redirects them to other directories.

## **Directory Descriptions**

The system works with 4 directories: in, out, bads and logs: 

* **IN**: Input directory of the project that receives only text files (**.txt**).

* **OUT**: Output directory for successfully processed files. In this case, everyone who has the word "key" in their content.

* **BADS**: Output directory for files processed with errors. In this case, everyone who does not have the word "key" in their content.

* **LOGS**: Directory for system log records.

> **Note**: If they do not exist, the system will create them automatically.

## **How to run the code**

Open the terminal and run the following command:

```
python script.py
```
