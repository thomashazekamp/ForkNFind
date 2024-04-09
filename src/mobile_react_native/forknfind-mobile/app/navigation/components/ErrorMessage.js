import {Alert} from 'react-native';

// Function ErrorMessage
// content - text that will be displayed when there is an error
const ErrorMessage = (content) => {

    return (
        Alert.alert("Error", content, [
            {text: 'OK', onPress: () => console.log('OK Pressed')}
          ])
    )
}

export default ErrorMessage;