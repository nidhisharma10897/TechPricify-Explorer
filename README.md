# TechPricify-Explorer

Project Description: Web Scraping for Alibaba Computer Hardware & Software Prices

This project is a web scraping application implemented using Flask, BeautifulSoup (bs4), and pandas to extract and display information about computer hardware and software prices from the Alibaba website.

Key Components:

1.Flask Web Application:                                                                                                                                           
• The project utilizes Flask, a web framework for Python, to create a simple web application.                                                                      
• The Flask app is configured to serve content on the root route ("/").

2.Web Scraping with BeautifulSoup:                                                                                                                                 
• The application opens a connection to the Alibaba webpage using urllib.request and retrieves the HTML content.                                                   
• BeautifulSoup (bs4) is employed to parse the HTML and navigate through the document's structure.                                                                

3.Data Extraction:                                                                                                                                                 
• The BeautifulSoup instance is used to locate HTML elements containing information about product names and prices on the Alibaba webpage.                         
• The 'p' and 'span' tags with specific class attributes are targeted to extract the names and prices of computer hardware and software.

4.Data Processing with Pandas:                                                                                                                                     
• The extracted information is organized into a list of dictionaries, where each dictionary corresponds to a product with its name and price.                      
• This list is then converted into a Pandas DataFrame for easy manipulation and analysis.

5.HTML Rendering:                                                                                                                                                  
• The Pandas DataFrame is converted to an HTML table using the 'to_html()' method.                                                                                 
• The resulting HTML table is returned as the content of the web page when a user accesses the root route.

6.Flask Web Server:                                                                                                                                                
• The Flask app runs a development server ('app.run(debug=True)') to serve the web application locally.                                                            

Execution:                                                                                                                                                         

• Upon accessing the root route ("/") of the Flask application, the web scraping process is triggered.                                                             
• The application fetches the HTML content from the Alibaba webpage related to computer hardware and software prices.                                              
• Relevant data (product names and prices) is extracted using BeautifulSoup.                                                                                       
• The extracted data is structured into a Pandas DataFrame.                                                                                                        
• The DataFrame is converted into an HTML table for easy presentation.                                                                                             
• The HTML table is then served as the content of the web page.                                                                                                   


Note:

The web scraping application is currently set to run in debug mode ('app.run(debug=True)'), suitable for development purposes.
This project serves as a practical example of web scraping for specific information and dynamically rendering it on a web page using Flask and Pandas.
