# Software Engineering -Summative-1

## Proposal

Within my role in the Department for Education on occasion mine and other teams are required to contact large numbers of MPs. MP contact details are publicly available through the parliamentary website however there is no easy method of retrieving all the required information, and therefore going through MP profiles one at a time is very time consuming. The proposal is to develop a web scraping tool that will use the Parliamentary website API (Parliament.uk, 2025) to retrieve the required information quickly. 

## Design
Initially this will be developed as a python script that can be run by individuals as need to produce a complete and up to date list of all sitting MPs. The intention is to add additional functionality, such as exporting the file in a desired format, adding the ability to filter the output by political party and create a GUI so that the tool is accessible to non-technical staff. Figure 1 demonstrates the initial GUI design created using Figma (Figma.com, 2025). 

(PIC)
Further functionally could be added such as the ability to view results in the app, include house of lords results and increase the number of filters available. But these considerations are outside the current scope of the project.  

## Plan
This project will be completed using an Agile methodology, using sprints to add features and fix bugs, whilst also producing the minimum viable product as soon as possible.  A test-driven development approach will also be used where appropriate to catch potential issues quickly (Yogesh, Vimala, 2020). 

To manage this project GitHub Projects will be used. Issues will be raised to provide tickets, these can be either for features to be added, or for testers to raise bug issues. Using a board view in the project, tickets can be progressed sequentially across the 4 categories (to do, in progress, in review, done). This way progress is tracked and all potential contributors to the projects can easily see at what stage each of the requirements is currently in. 

The requirements of the project will be listed at the start of the project, then using the agile method the most important tickets will be selected for that sprint. For a project this size the sprints would be relatively short, but will still contain the planning, implementation, review which will allow for the test-driven development method to catch potential issues within the sprint and retrospective phases. The minimum viable product can then be deployed and user testers allowed to give feedback. If the testers have proposals or bugs issues they can raise tickets, these may then in turn become priorities in the next sprint if they are urgent. The reason for using the Agile approach over other methods such as waterfall development is that there is a strong chance user requirements could change throughout the project life cycle, agile is more suited to developing software with changing requirements, with agile principles embracing changing customer needs (Agile manifesto, 2001). However, it is worth noting that there is no universal best approach to software development and that another project may be more suited to a non-agile approach (Kuhrmann, et al, 2022).

## Development
The first sprint of the project was used to address the three most important issues, which where to create the python file, create a working API request which would pull in the raw data and to then export that data in an Excel format. The reason these are the most important tickets is that they provide the minimum viable product by pulling the desired information from the website and putting into an accessible format that users could work with. This aligns with the agile methodology by producing a working product as fast as possible with the intention of then making improvements (Agile manifesto, 2001). As part of this sprint the test-driven development approach was used, both white box and black box testing were used with each having different advantages, such as black box testing allowing non-technical staff to test the product, and white box testing helping to optimize code (Verma, et al, 2017). The development team used white box to check the code for errors, and user testers used black box testing. Neither revealed issues however feedback for changes to be made was given in the form of two new issues; add a field for political party and change the output file type to CSV. 

The second sprint was used to address the two previously raised tickets. The reason for this is that these affected the minimum viable product as required by the end user and therefore took priority over other previously decided requirements. Again, these changes were put through testing. The user testing again revealed an issue which was that the output was returning too many results. There are 650 MPs in parliament, but the output was returning over 900 which is obviously incorrect. This issue was raised as a bug.  

The third sprint was used to address the bug raised in the previous round as this clearly affected the viability of the product, also this sprint added a function for the API request in addition to adding a date and time to the output folder for better auditing of outputs. The reason for turning the API request in to a function is that due to potential future additions to the programme it was decided that a functional style of programme would be easier to maintain by the users going forward (Zhang, et al, 2024). This also allows for unit testing and proper implementation of the test-driven developments approach as unit test can be run any time the code is changed to ensure functionality has not been inadvertently broken (Fang, et al (2023). User testing in this sprint produced a new issue from the testing team requesting improved performance as the programme ran very slowly on machines with lower performance.

The fourth sprint was used to improve the performance of the code by adding threading. This was in response the issue raised in the previous round of testing suggesting that the performance should be improved. This feature is currently in review with the changes still to be signed off from the test team. This sprint also contains the adding of a filter for political parties which is currently being worked on. Future sprints will add a GUI to make the user experience easier and take advantage of the filter added this sprint. 

## User Documentation

### Purpose:
This programme is used for retrieving the details of sitting MP across the UK. Using the parliamentary website API to pull up to date details of all MPs including name, title, constituency, email address and political   party

### Requirements:
To run this program Python must be installed. Python version used is 3.10.11. 
Libraires required for this script are: 
 *	Pandas – version 2.2.2
 *	Request – version 2.32.3
 * Datetime – Included with Python
 *	Concurrent.futures – Included with Python

### Using the Program: 
To use this programme, ensure all requirements are installed. Run the MP_Lookup_Tool.py file either in the terminal or in an IDE of your choice. No additional inputs are needed, the programme will produce a CSV file     with the naming convention “YYYYMMDD-mp_detail.csv” with the YYYYMMDD section representing the current Year month and day, this is done for auditing purposes. 

## Technical Documentation

### Requirements: 
To run this program Python must be installed. Python version used is 3.10.11. 
Libraires required for this script are: 
 *	Pandas – version 2.2.2
 *	Request – version 2.32.3
 *	Datetime – Included with Python
 *	Concurrent.futures – Included with Python

### API Details: 
The API used in this programme is available on the developer page of the parliamentary website found here: https://developer.parliament.uk/. There are number of APIs available the one used for this programme is the      members-api then under location use /api/Location/Constituency/Search. 

### Return Results:
The response from the API is store in a variable initialrequest and comes in a JSON format. This contain a large number of fields not all of which are relevant but could be extracted if required. From this the max       number of records is found, this value should equal 650. 

### Storing Results: 
To store the results, an empty pandas dataframe is used listing all the desired fields. The output file is also defined using the datetime library. The current day month and year is found using this library and          appended to the output file name using an f string.  Finally, an empty list called records is created, this will store the results of the function fetch_data and will in turn be used to populate the empty dataframe. 

### Fetch_data Function: 
The function takes an input of a number, this is due to the later use of threads and running multiple iteration of the function in parallel. Therefore, each parallel function needs to be working on different returned    results (More details on this in the threading section). A new response variable is created for the relevant number of records. This is stored in a JSON format in variable ‘items’. Using a for loop each item is          selected the relevant fields assigned to variables. 
Required fields:
 *	MPID
 *	nameDisplayAs
 *	nameFullTitle
 *	nameAddressAs
 *	constituencyName
 *	constituencyID
 *	party
 *	Email
  
For the email field this is not included in the existing request. A new request to the members API must be used. Using the MPID in the current iteration of the for loop a new request is made to               
"https://membersapi.parliament.uk/api/Members/"+str(MPid)+"/Contact". This is again returned in JSON format and the email field returned to a variable where possible, although some MPs don’t list an email address, in    these cases a null value is returned. All stored variables are then added to the records list as a dictionary. This results in a list of dictionaries, with each dictionary containing the detail for one MP. 

### Threading: 
To improve the performance of the programme threading is used. This uses the concurrent.futures library in particular the Threadexecutorpool. The max_workers must be stated, in this case 33 is the chosen number. The   reason for this is that MP records will be dealt with in batches of 20, since there are 650 MPs and 33 x 20 = 660 this means that all records will be selected as quickly as possible. A for loop is used with the range of the max number of MPs which should be 650, this range is broken down into groups of 20 and each will be assigned to a thread to work in parallel. The executor runs the fetch_data function with the previously established counter values as the input. 

### Returning Results: 
The records list of dictionaries is inserted into the blank dataframe previously created. The values if each record will be inserted into a row in the dataframe. The dataframe is then export as a CSV file using the existing filename naming convention.  

## Evaluation
The programme successfully achieves the basic requirements allowing users to quickly acquire all serving MP details. Several improvements were made to the minimum viable product version throughout the development life cycle, such as exporting result to a desired file format, and improving the performance of the programme with the addition of threading. This provides users with a working tool that performs adequately. 
However, it could be improved in several ways. Firstly, the completion of the remaining issues. Currently the program is only accessible using a Python script, whilst this is manageable for many more technically knowledgeable staff for many users this would be a barrier to entry and could cause issues. Therefore, completing the GUI aspect of the project would significantly improve this. However, a stage further would be to wrap the whole programme in an executable containing all the requirements. This would make the easiest to use solution for users. Also adding the ability to filter on political party would potentially reduce errors cause by users manually filtering the current output of the program. Therefore, this would be desirable to include if the project budget/timeline allows. Since this project is using the agile methodology producing a viable minimum product was the priority and additional feature will only be added if time and budget allow.  The Agile method of project management was appropriate for the project as it allowed for a flexible development considering changing user requirements.  And delivering a MVP as quickly as possible.  

The program takes advantage of functions, and therefore the ability to unit test allowing for the use of a test-driven development style. This helps identify issue early in the development cycle, helping lower the possibility of major bugs being found later when they are more difficult/expensive to fix. However, the use of functions could have been expanded further. For example, the conversion of both the records list to a dataframe and the dataframe to a csv file could both have been performed in a function. This would have allowed these to be include in the unit tests. 
In conclusion the product produced performs its requirement adequately. It was developed successfully using both the agile and test-driven development methodologies successfully using GitHub projects as the project management tool. There is scope to further develop the product to add functionality and increase useability. And in doing so refactor the existing code to further align with a test-driven style. 


## References
Agile manifesto. (2001). Available at: https://agilemanifesto.org/principles.html (Accessed 10 January 2025) 

Fang, et al (2023). “Effective Computer Software Unit Testing: Thinking about Unit Test-Driven Development (UTDD) Mode,” 12970:1297030-1297030–36. SPIE. Available at: https://doi.org/10.1117/12.3012428 (Accessed 18 January 2025)

Figma.com, 2025 Available at: https://www.figma.com/proto/51B72ZJcoVF3ewGDd5mRBg/MP-Lookup-GUI?node-id=0-1&t=bilt80owka6Wiydm-1 (Accessed 07 January 2025)

Kuhrmann, et al. (2022) “What Makes Agile Software Development Agile?” IEEE Transactions on Software Engineering 48, no. 9: 3523–39. Available at: https://doi.org/10.1109/TSE.2021.3099532 (Accessed 10 January 2025)

Parliament.uk, 2025, Available at: https://developer.parliament.uk/ (Accessed 05 January 2025) 

Verma, et al. (2017) “A Comparative Study of Black Box Testing and White Box Testing.” International Journal of Computer Sciences and Engineering 5, no. 12: 301–4. Available at: https://doi.org/10.26438/ijcse/v5i12.301304 (Accessed 10 January 2025)

Yogesh, T, and P Vimala. (2020). “Test-Driven Development of Automotive Software Functionality.” Third International Conference on Smart Systems and Inventive Technology (ICSSIT), 1162–65. IEEE. Available at: https://doi.org/10.1109/ICSSIT48917.2020.9214078 (Accessed 10 January 2025)

Zhang, et al. (2024) “Functional Programming Paradigm of Python for Scientific Computation Pipeline Integration.” Available at: https://arxiv.org/pdf/2405.16956 (Accessed 18 January 2025)





























