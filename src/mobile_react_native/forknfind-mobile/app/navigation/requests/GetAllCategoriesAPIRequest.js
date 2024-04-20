
// Function GetAllCategoriesAPIRequest
// setItemList - use state for saving data
const GetAllCategoriesAPIRequest = (setItemList) => {

    fetch("https://forknfind-fd07ce2d4651.herokuapp.com/api/category/", 
    {
        method: 'GET',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    }).then(response=>response.json())
    .then(data=>{

        // set the data using the item.category name
        setItemList(data.map(item => item.category));
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default GetAllCategoriesAPIRequest