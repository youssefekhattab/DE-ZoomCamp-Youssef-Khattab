schema = {
    "Sales_data" : [
      {"ORDERNUMBER": int(row[0]),
            "QUANTITYORDERED": int(row[1]),
            "PRICEEACH": float(row[2]),
            "ORDERLINENUMBER": int(row[3]),
            "SALES": str(row[4]),
            "ORDERDATE": datetime.strptime(row[8], '%d/%m/%Y/%H/%M'),
            "STATUS": str(row[5]),
            "QTR_ID": float(row[6]),
            "MONTH_ID": int(row[7]),
            "YEAR_ID": int(row[7]),
            "PRODUCTLINE": str(row[7]),
            "MSRP": int(row[7]),
            "PRODUCTCODE": str(row[7]),
            "CUSTOMERNAME": str(row[7]),
            "PHONE": str(row[7]),
            "ADDRESSLINE1": str(row[7]),
            "ADDRESSLINE2": str(row[7]),
            "CITY": str(row[7]),
            "STATE": str(row[9])
            "POSTALCODE": int(row[7]),
            "COUNTRY": str(row[7]),
            "TERRITORY": str(row[7]),
            "CONTACTLASTNAME": str(row[7]),
            "CONTACTFIRSTNAME": str(row[7]),
            "DEALSIZE": str(row[7]),
            }

    ]
}
