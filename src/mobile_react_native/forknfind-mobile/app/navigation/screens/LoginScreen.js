import React, { useState } from 'react';
import { View, Text, StyleSheet, TextInput, SafeAreaView, TouchableOpacity, StatusBar } from 'react-native';

import LoginAPIRequest from '../requests/LoginAPIRequest';

// Functional Component LoginScreen
// navigation - used to link to other screens created
// setIsLoggedIn - use state that will manage whether a use is logged in or not
export default function LoginScreen({ navigation, setIsLoggedIn }) {

    // Use states to manage the inputs to text boxes
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    // Logic for handling what happens when Sign In button is clicked
    const submitLogin = () => {

        console.log(setIsLoggedIn, username, password)
        // Pass to API request
        LoginAPIRequest({setIsLoggedIn, username, password})
    }

    // Logic for updating username use state
    const usernameUpdate = (text) => {

        setUsername(text)
    }

    // Logic for updating password use state
    const passwordUpdate = (text) => {

        setPassword(text)
    }

    return (
        <View style={{ flex: 1}}>
            <StatusBar barStyle="dark-content"/>
            <SafeAreaView style={{ flex: 1, backgroundColor: "white", alignItems: 'center', justifyContent: 'center' }}>
                <View style={styles.loginBoxContainer}>
                    <Text style={styles.heading}>
                        Sign In
                    </Text>
                    <Text style={styles.subHeading}>
                        Welcome back, you've been missed!
                    </Text>
                    <Text style={styles.textBoxHeading}>
                        Username
                    </Text>
                    {/* Text input for putting the username in, on update it passed to the logic handler */}
                    <TextInput 
                        placeholder="username"
                        placeholderTextColor="#797979"
                        autoCapitalize='none'
                        style={styles.textBox}
                        autoCorrect={false}
                        value={username} 
                        onChangeText={usernameUpdate}
                        >
                    </TextInput>
                    <Text style={[styles.textBoxHeading, {marginTop: "5%"}]}>
                        Password
                    </Text>
                    <TextInput 
                        placeholder="password"
                        placeholderTextColor="#797979"
                        autoCapitalize='none'
                        style={styles.textBox}
                        autoCorrect={false}
                        value={password} 
                        onChangeText={passwordUpdate}
                        secureTextEntry={true}
                        >
                    </TextInput>
                    {/* On click of button passes to the API request function */}
                    <TouchableOpacity style={styles.loginButton} onPress={() => submitLogin()}>
                        <Text style={styles.buttonText}>Sign In</Text>
                    </TouchableOpacity>
                    {/* Link allowing users to move to the create account screen if they do not have an account */}
                    <Text style={[styles.subHeading, {marginTop: "18%"}]}>
                        Don't have an account? <Text onPress={() => navigation.navigate('CreateAccount')} style={styles.linkerText} >Sign Up</Text> 
                    </Text>
                </View>
            </SafeAreaView>
        </View>
    );
}

const styles = StyleSheet.create ({

    // Login box container holding information
    loginBoxContainer: {
        height: "55%",
        width: "80%",
    },
    // Heading text for the word Sign In
    heading: {
        fontWeight: '400',
        fontSize: 35,
        color: '#000000',
        alignSelf: 'center',
        paddingBottom: "3%",
    },
    // Sub Heading text for the Welcome back...
    subHeading: {
        fontWeight: '400',
        fontSize: 15,
        color: '#525357',
        alignSelf: 'center',
        paddingBottom: "10%",
    },
    // Headings for the titles above the text inputs
    textBoxHeading: {
        fontWeight: '700',
        fontSize: 16,
        color: '#525357',
        paddingBottom: '1%',
    },
    // Text box css
    textBox: {
        color: 'black',
        paddingHorizontal: 20,
        paddingVertical: 8,
        borderRadius: 10,
        fontSize: 16,
        fontWeight: '500',
        borderWidth: 2,
        borderColor: "#525357",
    },
    // Login button css
    loginButton: {
        width: '100%',
        top: '8%',
        height: 57,
        backgroundColor: '#1C58F2',
        borderRadius: 20,

        justifyContent: 'center',
        alignItems: 'center',
    },
    // Login button text css
    buttonText: {
        textAlign: 'center',
        fontSize: 25,
        fontWeight: '600',
        color: 'white'
    },
    // Linker text css linking login to create account
    linkerText: {
        color: 'blue',
        textDecorationLine: 'underline',
    },

})