utils docomentation 
1. read_csv :
    agr: "path" --> path of the csv file 
    returen : loaded csv file 

2. colume_chk : 
   
    args: data01,data02 are pandas dataframe
    return: same columns in data01 and data02 and count of columns
    
3. api_call :
    Make API call and return response
    Args:
        url (str): URL to make the API call
        method (str): HTTP method to use
        data (dict): Data to pass to the API call
        headers (dict): Headers to pass to the API call
        params (dict): Parameters to pass to the API call

    Returns:
        dict: Response from the API call