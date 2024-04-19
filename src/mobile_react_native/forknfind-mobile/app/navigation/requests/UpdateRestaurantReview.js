import ErrorMessage from '../components/ErrorMessage';

// Function UpdateRestaurantReview
// id - review id
// text - text information inputted by user
// rating - rating information inputted by user
// setResponse - setting the response if the review was successful
const UpdateRestaurantReview = (id, text, rating, setResponse) => {

    console.log(id, text, rating)

    fetch("https://lionfish-dear-roughy.ngrok-free.app/review/change/" + id + "/", 
    {
        method: 'PATCH',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_global,
    }, body: JSON.stringify({"description": text, "rating": rating}),
    }).then(response=>response.json())
    .then(data=>{

        if (data['description'] == "This field may not be blank.") {
            ErrorMessage(content="Description field may not be blank.")
        }

        if (data["rating"] == rating && data["description"] == text ) {
            setResponse("success");
        }
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default UpdateRestaurantReview