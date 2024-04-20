import ErrorMessage from '../components/ErrorMessage';

// Function CreateRestaurantReview
// id - restaurant id
// text - text information inputted by user
// rating - rating information inputted by user
// setResponse - setting the response if the review was successful
const CreateRestaurantReview = (id, text, rating, setResponse) => {

    console.log(id, text, rating)

    fetch("https://forknfind-fd07ce2d4651.herokuapp.com/register/review/", 
    {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_global,
    }, body: JSON.stringify({"description": text, "rating": rating, "restaurant": id}),
    }).then(response=>response.json())
    .then(data=>{

        if (data['description'] == "This field may not be blank.") {
            ErrorMessage(content="Description field may not be blank.")
        }

        if (data["rating"] == rating && data["restaurant"] == id ) {
            setResponse("success");
        }
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default CreateRestaurantReview