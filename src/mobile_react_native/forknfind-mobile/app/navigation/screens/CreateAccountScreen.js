import React, { useState } from 'react';
import { View, Text, StyleSheet, TextInput, SafeAreaView, TouchableOpacity, StatusBar } from 'react-native';

import CreateAccountAPIRequest from '../requests/CreateAccountAPIRequest';

// Functional Component CreateAccountScreen
// navigation - used to link to other screens created
// setIsLoggedIn - use state that will manage whether a use is logged in or not
export default function CreateAccountScreen({ navigation, setIsLoggedIn }) {

    // Use states to manage the inputs to text boxes
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState("")
    const [passwordCheck, setPasswordCheck] = useState("")

    // Logic for handling what happens when Sign Up button is clicked
    const submitLogin = () => {

        console.log(setIsLoggedIn, username, password)
        // Check to maek sure passwords inputted are the same value
        if (password == passwordCheck) {
            // Pass to API request
            CreateAccountAPIRequest({setIsLoggedIn, username, password, email, firstName, lastName})
        }
        else {
            console.log("passwords not the same i think")
        }
    }

    // Logic for updating username use state
    const usernameUpdate = (text) => {

        setUsername(text)
    }

    // Logic for updating password use state
    const passwordUpdate = (text) => {

        setPassword(text)
    }

    // Logic for updating firstName use state
    const firstNameUpdate = (text) => {

        setFirstName(text)
    }

    // Logic for updating lastName use state
    const lastNameUpdate = (text) => {

        setLastName(text)
    }

    // Logic for updating email use state
    const emailUpdate = (text) => {

        setEmail(text)
    }

    // Logic for updating passwordCheck use state
    const passwordCheckUpdate = (text) => {

        setPasswordCheck(text)
    }


    return (
        <View style={{ flex: 1}}>
            <StatusBar barStyle="dark-content"/>
            <SafeAreaView style={{ flex: 1, backgroundColor: "white", alignItems: 'center', justifyContent: 'center' }}>
                <View style={styles.createAccountBoxContainer}>
                    <Text style={styles.heading}>
                        Create Account
                    </Text>
                    <Text style={styles.subHeading}>
                        Fill in your information to register an account
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
                    <View style={styles.splitScreen}>
                        <View style={{width: "47.5%"}}>
                            <Text style={[styles.textBoxHeading, {marginTop: 15}]}>
                                First Name
                            </Text>
                            <TextInput 
                                placeholder="first name"
                                placeholderTextColor="#797979"
                                autoCapitalize='none'
                                style={styles.textBox}
                                autoCorrect={false}
                                value={firstName} 
                                onChangeText={firstNameUpdate}
                                >
                            </TextInput>
                        </View>
                        <View style={{width: "47.5%"}}>
                            <Text style={[styles.textBoxHeading, {marginTop: 15}]}>
                                Last Name
                            </Text>
                            <TextInput 
                                placeholder="last name"
                                placeholderTextColor="#797979"
                                autoCapitalize='none'
                                style={styles.textBox}
                                autoCorrect={false}
                                value={lastName} 
                                onChangeText={lastNameUpdate}
                                >
                            </TextInput>
                        </View>
                    </View>
                    <Text style={[styles.textBoxHeading, {marginTop: 15}]}>
                        Email
                    </Text>
                    <TextInput 
                        placeholder="password"
                        placeholderTextColor="#797979"
                        autoCapitalize='none'
                        style={styles.textBox}
                        autoCorrect={false}
                        value={email} 
                        onChangeText={emailUpdate}
                        >
                    </TextInput>
                    <Text style={[styles.textBoxHeading, {marginTop: 15}]}>
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
                    <Text style={[styles.textBoxHeading, {marginTop: 15}]}>
                        Retype Password
                    </Text>
                    <TextInput 
                        placeholder="retype password"
                        placeholderTextColor="#797979"
                        autoCapitalize='none'
                        style={styles.textBox}
                        autoCorrect={false}
                        value={passwordCheck} 
                        onChangeText={passwordCheckUpdate}
                        secureTextEntry={true}
                        >
                    </TextInput>
                    {/* On click of button passes to the API request function */}
                    <TouchableOpacity style={styles.loginButton} onPress={() => submitLogin()}>
                        <Text style={styles.buttonText}>Sign Up</Text>
                    </TouchableOpacity>
                    {/* Link allowing users to move to the login screen if they have an account */}
                    <Text style={[styles.subHeading, {marginTop: "18%"}]}>
                        Already have an account? <Text onPress={() => navigation.navigate('Login')} style={styles.linkerText} >Sign In</Text> 
                    </Text>
                </View>
            </SafeAreaView>
        </View>
    );
}

const styles = StyleSheet.create ({

    // Create Account box container holding information
    createAccountBoxContainer: {
        height: "75%",
        width: "80%",
    },
    // Heading text for the word Sign Up
    heading: {
        fontWeight: '400',
        fontSize: 35,
        color: '#000000',
        alignSelf: 'center',
        paddingBottom: "3%",
    },
    // Sub Heading text for the fill in your...
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
    // Split screen CSS for the first name and last name inputs
    splitScreen: {
        flexDirection: 'row', 
        justifyContent: 'space-between',
    },
    linkerText: {
        color: 'blue',
        textDecorationLine: 'underline',
    },
})