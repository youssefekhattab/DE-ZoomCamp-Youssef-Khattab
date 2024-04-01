schema = {
    "Sales_data" : [
      {"invoice_no": str(row[0]),
            "customer_id": str(row[1]),
            "gender": str(row[2]),
            "age": int(row[3]),
            "category": str(row[4]),
            "quantity": str(row[5]),
            "price": float(row[6]),
            "payment_method": str(row[7]),
            "invoice_date": datetime.strptime(row[8], '%d/%m/%Y'),
            "shopping_mall": str(row[9])
            }

    ]
}
