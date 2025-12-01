
final_df = (
    df[df['Quantity'] >= 2]                            
      .query("Category == 'Apparel'")                   
      .assign(TotalValue=lambda x: x['Quantity'] * x['UnitPrice'])  
      .sort_values(by='TotalValue', ascending=False)    
      .reset_index(drop=True)                           
)

print(final_df)
