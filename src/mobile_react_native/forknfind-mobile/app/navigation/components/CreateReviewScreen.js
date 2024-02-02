import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Modal, TouchableOpacity, SafeAreaView, StatusBar} from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { ScrollView, TextInput } from 'react-native-gesture-handler';
import CreateRestaurantReview from '../requests/CreateRestaurantReview';

// Functional Component CreateReviewScreen
// visible - use state identifying whether the modal is visible or not
// onClose - the trigger for closing the modal view
// id - id of a restaurant that can be passed in when creating a review
const CreateReviewScreen = ({ visible, onClose, id }) => {

    // Each use state is for identify what is the highest number of stars given to the restaurant review
    const [starOne, setStarOne] = useState(true);
    const [starTwo, setStarTwo] = useState(false);
    const [starThree, setStarThree] = useState(false);
    const [starFour, setStarFour] = useState(false);
    const [starFive, setStarFive] = useState(false);
    const [inputValue, setInputValue] = useState('');
    const [response, setResponse] = useState('');

    // function for updating which stars have a yellow in them
    const updateStars = (number) => {

        if (number == 1) {
            setStarOne(true)
            setStarTwo(false)
            setStarThree(false)
            setStarFour(false)
            setStarFive(false)
        } else if (number == 2) {
            setStarOne(true)
            setStarTwo(true)
            setStarThree(false)
            setStarFour(false)
            setStarFive(false)
        } else if (number == 3) {
            setStarOne(true)
            setStarTwo(true)
            setStarThree(true)
            setStarFour(false)
            setStarFive(false)
        } else if (number == 4) {
            setStarOne(true)
            setStarTwo(true)
            setStarThree(true)
            setStarFour(true)
            setStarFive(false)
        } else if (number == 5) {
            setStarOne(true)
            setStarTwo(true)
            setStarThree(true)
            setStarFour(true)
            setStarFive(true)
        }
    };

    // Handles the text input
    const handleInputValue = (text) => {
        setInputValue(text);
    };

    // Create review not implement in current state
    const createReview = () => {

        if (starFive == true) {
            CreateRestaurantReview(id, inputValue, 5, setResponse)
        } else if (starFour == true) {
            CreateRestaurantReview(id, inputValue, 4, setResponse)
        } else if (starThree == true) {
            CreateRestaurantReview(id, inputValue, 3, setResponse)
        } else if (starTwo == true) {
            CreateRestaurantReview(id, inputValue, 2, setResponse)
        } else {
            CreateRestaurantReview(id, inputValue, 1, setResponse)
        }
    }

    useEffect(() => {

        console.log(response)

        if (response == "success") {
            onClose();
            setResponse("");
        }
    }, [response]);

    // Component Returns a modal view
    return (
        // Sets the modal props
        <Modal
            animationType="slide"
            transparent={false}
            visible={visible}
            onRequestClose={onClose}
        >
        {/* Set the status bar icons to dark mode */}
        <StatusBar barStyle="dark-content" />
            {/* Set the top safeareaview to be white, needed for newer iphones with dynamic island */}
            <SafeAreaView style={{ backgroundColor: "white" }} />
            <ScrollView>
                {/* Set the top background colour and the height of page */}
                <View style={styles.mainContainer}>
                    <View style={styles.backContainer}>
                        <View>
                            {/* Surround the back button in a touchable button so when clicked the modal is exited */}
                            <TouchableOpacity onPress={onClose}>
                                <AntDesign name="arrowleft"  size={28} color={"black"} style={{paddingTop: '5%'}}/>
                            </TouchableOpacity>
                        </View>
                    </View>
                    {/* Name of Restaurant */}
                    <View style={styles.titleContainer}>
                        <Text style={styles.restaurantTitleText}>
                            33 Cafe Skerries
                        </Text>
                    </View>
                    {/* address of Restaurant */}
                    <View style={styles.addressContainer}>
                        <Text style={styles.restaurantAddressText}>
                            98 Strand St, Townparks, Skerries, Co. Dublin K34 V300, Ireland
                        </Text>
                    </View>
                    {/* Container break, breaks up the content and adds a gap between */}
                    <View style={styles.containerBreak}/>
                    {/* Heading for giving user rating */}
                    <View style={styles.informationContainer}>
                        <Text style={styles.informationHeadingText}>Your Rating</Text>
                    </View>
                    {/* Star code, each individual star is checked to see if the yellow should be appearing if it is selected */}
                    <View style={styles.starContainer}>
                        <TouchableOpacity style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]} onPress={() => updateStars(1)}>
                            { starOne ? (<AntDesign name="star" size={40} color="#DBFF00" style={{position: 'absolute'}}/>) : (<View/>)}
                            <AntDesign name="staro" size={40} color="#000000" style={{position: 'absolute'}}/>
                        </TouchableOpacity>
                        <TouchableOpacity style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]} onPress={() => updateStars(2)}>
                            { starTwo ? (<AntDesign name="star" size={40} color="#DBFF00" style={{position: 'absolute'}}/>) : (<View/>)}
                             <AntDesign name="staro" size={40} color="#000000" style={{position: 'absolute'}}/>
                        </TouchableOpacity>
                        <TouchableOpacity style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]} onPress={() => updateStars(3)}>
                            { starThree ? (<AntDesign name="star" size={40} color="#DBFF00" style={{position: 'absolute'}}/>) : (<View/>)}
                            <AntDesign name="staro" size={40} color="#000000" style={{position: 'absolute'}}/>
                        </TouchableOpacity>
                        <TouchableOpacity style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]} onPress={() => updateStars(4)}>
                            { starFour ? (<AntDesign name="star" size={40} color="#DBFF00" style={{position: 'absolute'}}/>) : (<View/>)}
                            <AntDesign name="staro" size={40} color="#000000" style={{position: 'absolute'}}/>
                        </TouchableOpacity>
                        <TouchableOpacity style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]} onPress={() => updateStars(5)}>
                            { starFive ? (<AntDesign name="star" size={40} color="#DBFF00" style={{position: 'absolute'}}/>) : (<View/>)} 
                            <AntDesign name="staro" size={40} color="#000000" style={{position: 'absolute'}}/>
                        </TouchableOpacity>
                    </View>
                    {/* Text box for adding description */}
                    <View style={styles.textContainer}>
                        <Text style={styles.reviewHeadingText}>Add detailed Review</Text>
                        <TextInput style={styles.textInputContainer} placeholder="Enter here" textAlignVertical="top" multiline={true} value={inputValue} onChangeText={handleInputValue}/>
                    </View>
                </View>
            </ScrollView>
            {/* Button for submitting the review, currently doesnt funciton api not set up */}
            <TouchableOpacity style={styles.reviewButton} onPress={() => createReview({id})}>
                <Text style={styles.buttonText}>Submit</Text>
            </TouchableOpacity>
        </Modal>);
}

// Style code
const styles = StyleSheet.create({
    // Main container that surrounds the screen
    mainContainer: {
        backgroundColor: '#F5F7FC',
        height: '100%',
    },
    // Goes behind the back icon to position it correctly
    backContainer: {
        flexDirection: 'row',
        paddingLeft: '10%',
        width: '100%',
        backgroundColor: 'white',
    },
    // Container for the title
    titleContainer: {
        paddingTop: '5%',
        paddingLeft: '10%',
        paddingRight: '10%',
        width: '100%',
        backgroundColor: 'white',
    },
    // Styling for Restaurant Name
    restaurantTitleText: {
        fontWeight: '500',
        fontSize: 30,
        color: '#000000'
    },
    // Container for the address
    addressContainer: {
        paddingTop: '1%',
        paddingLeft: '10%',
        paddingRight: '10%',
        width: '100%',
        backgroundColor: 'white',
        paddingBottom: '4%',
    },
    // Styling for Restaurant Address
    restaurantAddressText: {
        fontWeight: '500',
        fontSize: 16,
        color: '#525357'
    },
    // Container break code to split up the containers
    containerBreak: {
        width: '100%',
        height: 20,
        backgroundColor: '#F5F7FC',
    },
    // Information container holding stars and review
    informationContainer: {
        paddingTop: '4%',
        width: '100%',
        backgroundColor: 'white',
    },
    // Heading for your rating
    informationHeadingText: {
        fontWeight: '700',
        fontSize: 16,
        color: '#525357',
        paddingBottom: '4%',
        alignSelf: 'center',
    },
    // Container for holding the stars in the a horizontal line, important to use "flexDirection: 'row'"
    starContainer: {
        paddingTop: '4%',
        paddingLeft: '15%',
        paddingRight: '15%',
        width: '100%',
        backgroundColor: 'white',
        flexDirection: 'row',
        paddingBottom: '12%',
    },
    // Width betweens stars
    starSection: {
        width: '20%',
    },
    // Heading for the review
    reviewHeadingText: {
        fontWeight: '700',
        fontSize: 16,
        color: '#525357',
        paddingBottom: '3%',
    },
    // Text container for review description
    textContainer: {
        paddingLeft: '10%',
        paddingRight: '10%',
        width: '100%',
        backgroundColor: 'white',
    },
    // Text input for review description
    textInputContainer: {
        backgroundColor: '#F5F7FC',
        height: 150,
        borderRadius: 10,
        padding: 15,
        fontSize: 17,
    },
    // Review Button styling
    reviewButton: {
        position: 'absolute',
        width: '74%',
        top: '87%',
        height: '7%',
        backgroundColor: '#1C58F2',
        left: '13%',
        borderRadius: 20,

        justifyContent: 'center',
        alignItems: 'center',
    },
    // Text for button
    buttonText: {
        textAlign: 'center',
        fontSize: 25,
        fontWeight: '600',
        color: 'white'
    },
});

export default CreateReviewScreen;