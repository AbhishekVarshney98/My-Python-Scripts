from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\python scripts\Whatsapp send messages\chromedriver.exe")
# driver.get("https://ctazuresmartenterprise.azurewebsites.net/")
# driver.get("https://celebalrnd.azurewebsites.net/")
driver.get("https://celebal-sca.azurewebsites.net/")

l1=["CustomerName","SubscriptionID","TenantID","ClientID","ClientSecret","ResourceGroupName","AppServiceName",
   "AppServiceURL","DataFactoryName","StorageAccountName","StorageAccessKey","StorageConnectionString","SQLServerName","SQLUserName","SQLPassword",
   "SQLDatabaseName","SQLConnectionString","DataBricksName","DataBricksToken","DataBricksScope","DataBricksWorkspaceURL",
   "PowerBIEmbeddedName","PowerBIEmbeddedAdmin","KeyVaultName","AzureFunctionURL"]

l2 = ["Abhishek Varshney","98b7f374-098f-4d1e-98d1-a2ca9fc58c4c","e4e34038-ea1f-4882-b6e8-ccd776459ca0","66a117c7-1ccf-4729-a55a-c8d0a355e821",
      "boIO3kkL-dhv3qwM2:6x-wgParIn?46@","CTAzureSmartEnterpriseSKU1","sca-celebal",
      "https://sca-celebal.azurewebsites.net","CTAzureSmartEnterpriseadf66","ctazuresmartenterprisesa",
      "p42oSJW3JdFKpWwpPXn+5seZqVLoCpFQzxu8rHlWgv/SY4IR4mT/m9MHFt8lMCCroQxhG3Dywv/Yz/c10EtNIg==",
      "DefaultEndpointsProtocol=https;AccountName=ctazuresmartenterprisesa;AccountKey=p42oSJW3JdFKpWwpPXn+5seZqVLoCpFQzxu8rHlWgv/SY4IR4mT/m9MHFt8lMCCroQxhG3Dywv/Yz/c10EtNIg==;EndpointSuffix=core.windows.net",
      "ctazuresmartenterpriseserver.database.windows.net","celebal","password@123","ctazuresmartenterprisedb",
      "Server=tcp:ctazuresmartenterpriseserver.database.windows.net,1433;Initial Catalog=ctazuresmartenterprisedb;Persist Security Info=False;User ID=celebal;Password=password@123;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;",
      "CTAzureSmartEnterprisedbr","dapic52387522718d38b805947530bbc36f1","scope","https://centralus.azuredatabricks.net",
      "ctazuresmartenterprisepbi","Murtaza","keyscact44","https://ctazuresmartenterprisefuncapp.azurewebsites.net/api/createschemaindwh?code=h9qtGYbzMdsBDZuAQG6/s5R00xvqvA3UJMqF0mZ/9nULL7yMd0irPQ=="]

for i,j in zip(l1,l2):
    ex=driver.find_element_by_id(i)
    ex.clear()
    ex.send_keys(j) 


    
l2=["BQProject","BQClientID","BQClientSecret","BQToken","BQTableSchema","BQTables"]
for i in l2:
    ex=driver.find_element_by_name(i)
    ex.clear()
    ex.send_keys("Abhishek Varshney") 
    # ex.send_keys(Keys.RETURN)

# ex.send_keys(Keys.RETURN)
ee=input("enter any thing to close")
driver.quit()
