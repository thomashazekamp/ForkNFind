
// Function CreateRestaurantReview
// id - restaurant id
// text - text information inputted by user
// rating - rating information inputted by user
// setResponse - setting the response if the review was successful
const CreateRestaurantReview = (id, text, rating, setResponse) => {

    console.log(id, text, rating)

    fetch("http://192.168.1.82:8000/register/review/", 
    {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_global,
    }, body: JSON.stringify({"description": text, "rating": rating, "restaurant": id}),
    }).then(response=>response.json())
    .then(data=>{

        console.log(data)
        console.log(data["description"] == text)
        console.log(data["rating"] == rating)
        console.log(data["restaurant"] == id)
        if (data["description"] == text && data["rating"] == rating && data["restaurant"] == id ) {
            setResponse("success");
        }
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default CreateRestaurantReview