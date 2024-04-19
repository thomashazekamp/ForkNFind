import ErrorMessage from '../components/ErrorMessage';
import LoginAPIRequest from "./LoginAPIRequest";

// Function CreateAccountAPIRequest
// setIsLoggedIn - use state passed in that will be updated if the login is successful
// username - the username inputted by the user
// password - the password inputted by the user
// email - the email inputted by the user
// firstName - the firstName inputted by the user
// lastName - the lastName inputted by the user
const CreateAccountAPIRequest = ({setIsLoggedIn, username, password, email, firstName, lastName}) => {

    console.log(JSON.stringify({username: username, password: password, email: email, first_name: firstName, last_name: lastName}))

    // Fetch the API with this information
    fetch("https://lionfish-dear-roughy.ngrok-free.app/register/user/", 
    {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        },
        body: JSON.stringify({username: username, password: password, email: email, first_name: firstName, last_name: lastName})
    }).then(response=>response.json())
    .then(data=>{

        if (data['username'] == "This field may not be blank.") {
            ErrorMessage(content="Username field may not be blank.")
        } else if (data['first_name'] == "This field may not be blank.") {
            ErrorMessage(content="First Name field may not be blank.")
        } else if (data['last_name'] == "This field may not be blank.") {
            ErrorMessage(content="Last Name field may not be blank.")
        } else if (data['email'] == "This field may not be blank.") {
            ErrorMessage(content="Email field may not be blank.")
        } else if (data['password'] == "This field may not be blank.") {
            ErrorMessage(content="Password field may not be blank.")
        } else if (data['username'] == "This username is already in use.") {
            ErrorMessage(content="This username is already in use.")
        }

        // if the API was a success then login to the users account with the new information
        if (data['username'] == username && data['email'] == email && data['first_name'] == firstName && data['last_name'] == lastName) {
            LoginAPIRequest({setIsLoggedIn, username, password})
        }
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default CreateAccountAPIRequest