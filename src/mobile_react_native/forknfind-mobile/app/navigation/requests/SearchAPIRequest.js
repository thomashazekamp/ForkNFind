
// Function CreateAccountAPIRequest
// searchQueryRef - search query information
// setData - for setting the data
// setOriginalData - for setting the data as a backup
const SearchAPIRequest = (searchQueryRef, setData, setOriginalData, location) => {

    var searchString = "?";

    // loop through the search query information combing it together to maek 1 long query
    for (const [key,value] of Object.entries(searchQueryRef.current)){

        if (!(value == "" || value == false)) {
            searchString += key + "=" + value + "&"
        }
        console.log(key, value);
        console.log(searchString);
    }

    // add it to the end of the url
    fetch("http://192.168.1.82:8000/search/restaurant/" + location.latitude + "/" + location.longitude + "/" + searchString, 
    {
        method: 'GET',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    }).then(response=>response.json())
    .then(data=>{

        // set the data once its returned
        setData(data)
        setOriginalData(data)
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default SearchAPIRequest