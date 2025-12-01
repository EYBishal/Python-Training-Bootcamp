pivot_table = df.pivot_table(
    index='Category',            
    columns='PaymentMethod',     
    values='TotalPrice',         
    aggfunc='sum',               
    fill_value=0                 
)

print(pivot_table)
