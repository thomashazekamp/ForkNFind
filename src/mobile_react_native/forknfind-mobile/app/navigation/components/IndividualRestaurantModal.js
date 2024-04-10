import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, Modal, TouchableOpacity, SafeAreaView, StatusBar, ActivityIndicator } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { ScrollView } from 'react-native-gesture-handler';
import CreateReviewScreen from './CreateReviewScreen';
import IndividualRestaurantAPIRequest from '../requests/IndividualRestaurantAPIRequest';
import ContentRecommendationsAPIRequest from '../requests/ContentRecommendationsAPIRequest';
import AsyncStorage from '@react-native-async-storage/async-storage';
import RestaurantCard from './RestaurantCard';
import GetAllRestaurantReviews from '../requests/GetAllRestaurantReviews';
import ReviewSortBy from '../components/ReviewSortBy'
import SplitCapitalise from '../components/SplitCapitalise';
import ReviewRestaurantList from './ReviewRestaurantList';

// Functional Component CreateAccountScreen
// visible - wether modal is visible or not
// onClose - how to close the modal
// id - id of restaurant 
// distance - distance from user to restaurant
const IndividualRestaurantModal = ({ visible, onClose, id, distance }) => {

    // Use states for restaurant information
    const [restaurantData, setRestaurantData] = useState(null)
    const [modalVisible, setModalVisible] = useState(false);
    const [restaurantRecommendationData, setRestaurantRecommendationData] = useState([]);
    const [location, setLocation] = useState(null);

    // Review use states
    const [data, setData] = useState([]);
    const [originalData, setOriginalData] = useState(data);
    const [selectedReviews, setSelectedReviews] = useState("all");
    const [modalSortVisible, setModalSortVisible] = useState(false);
    const [sortVisual, setSortVisual] = useState("All Relevance");

    const changeSort = () => {

        setModalSortVisible(!modalSortVisible);
    }

    // function for comparing specific dates
    const compareDates = (a, b) => {
        var dateA = new Date(a.date);
        var dateB = new Date(b.date);
      
        
        if (dateA > dateB) {
            return -1
        } else if (dateA < dateB) {
            return 1
        }
        return 0;
    };

    // Use effect for when the type of reviews selected are changed or the sorting is changed
    useEffect(() => {

        // Get all the review data
        if (originalData == null) { return }
        const array = Object.values(originalData);

        // Sort the user data based on the inputted filter

        if (sortVisual == "Ratings (Ascending)") {
    
            // Sort the data such that the lowest ratings are first and gradually getting higher
            array.sort((a, b) => a.rating - b.rating);
    
        } else if (sortVisual == "Ratings (Descending)") {
    
            array.sort((a, b) => b.rating - a.rating);

        } else if (sortVisual == "Date (Recent)") {
    
            array.sort((a, b) => compareDates(a, b));

        } else if (sortVisual == "Date (Oldest)") {
    
            array.sort((a, b) => compareDates(b, a));
        }

        // Filter the user data based on the current selection
        if (selectedReviews == "positive") {
            
            // Only keep the reviews with sentiment of 1
            setData(array.filter(item => item.sentiment === 1))

        } else if (selectedReviews == "all") {
    
            setData(array)
    
        } else if (selectedReviews == "negative") {
            
            // Only keep the reviews with sentiment of 0
            setData(array.filter(item => item.sentiment === 0))

        } 
    }, [selectedReviews, sortVisual]);
   
    // Use effect for getting restaurant information on startup
    useEffect(() => {

        const retrieveLocation = async () => {
            try {
                const latitude = await AsyncStorage.getItem('locationDataLatitude');
                const longitude = await AsyncStorage.getItem('locationDataLongitude');
                if (latitude !== null && longitude !== null) {
                    return {latitude, longitude}
                }
                } catch (error) {
                    console.log(error)
            }
        }
    
        const fetchLocationData = async () => {
            const locationData = await retrieveLocation();
            setLocation(locationData);
            ContentRecommendationsAPIRequest(setRestaurantRecommendationData, id, locationData);
        };
        
        IndividualRestaurantAPIRequest(id, setRestaurantData);
        GetAllRestaurantReviews(id, setData, setOriginalData)
        fetchLocationData();
    }, []);

    // Converting the opening times to user friendly formats
    const getOpeningTime = (day) => {

        // If the status is closed then return closed, else make the opening or closing time string
        if (day["open"] == false) {
            return "Closed"
        }
        returnString = ""
        if (day["open_time"]["hour"] < 10 && day["open_time"]["hour"] >= 0) {
            returnString = '0' + day["open_time"]["hour"].toString();
        } else {
            returnString = day["open_time"]["hour"].toString()
        }
        returnString += ":"
        if (day["open_time"]["minute"] < 10 && day["open_time"]["minute"] >= 0) {
            returnString += '0' + day["open_time"]["minute"].toString();
        } else {
            returnString += day["open_time"]["minute"].toString()
        }
        returnString += " - "
        if (day["close_time"]["hour"] < 10 && day["close_time"]["hour"] >= 0) {
            returnString += '0' + day["close_time"]["hour"].toString();
        } else {
            returnString += day["close_time"]["hour"].toString()
        }
        returnString += ":"
        if (day["close_time"]["minute"] < 10 && day["close_time"]["minute"] >= 0) {
            returnString += '0' + day["close_time"]["minute"].toString();
        } else {
            returnString += day["close_time"]["minute"].toString()
        }

        return returnString
        
    }    

    // Review modal is visible or not
    const toggleModal = () => {
        setModalVisible(!modalVisible);
    }

    return (
        <Modal
            animationType="slide"
            transparent={false}
            visible={visible}
            onRequestClose={onClose}
        >
            {restaurantData == null ? 
                <View style={{
                    flex: 1, 
                    alignItems: 'center',
                    justifyContent: 'center', 
                }}> 
                    <ActivityIndicator size="large" color="#1C58F2" />
                </View>
            :
            <View>
            <StatusBar barStyle="dark-content" />
            <SafeAreaView style={{ backgroundColor: "white" }} />
            <ScrollView>
                <View style={styles.mainContainer}>
                        <View style={styles.backContainer}>
                            <View>
                                <TouchableOpacity onPress={onClose}>
                                    <AntDesign name="arrowleft"  size={28} color={"black"} style={{paddingTop: '5%'}}/>
                                </TouchableOpacity>
                            </View>
                        </View>
                        <View style={styles.titleContainer}>
                            <Text style={styles.restaurantTitleText}>
                                {restaurantData["name"]}
                            </Text>
                        </View>
                        <View style={styles.addressContainer}>
                            <Text style={styles.restaurantAddressText}>
                                {restaurantData["address"]}
                            </Text>
                        </View>
                        <View style={styles.containerBreak}/>
                        <View style={styles.informationContainer}>
                            <View style={styles.leftInformationContainer}>
                                <Text style={styles.informationHeadingText}>Rating</Text>
                                <Text style={[styles.informationContentText, {paddingLeft: '13%'}]}>{restaurantData["average_rating"]}/5 ({restaurantData["review_number"]})</Text>
                                <AntDesign name="star" size={22} color="#DBFF00" style={{position: 'absolute',paddingLeft: "24%", paddingTop: "14%"}} />
                                <AntDesign name="staro" size={22} color="#000000" style={{position: 'absolute',paddingLeft: "24%", paddingTop: "14%"}} />
                            </View>
                            <View style={styles.rightInformationContainer}>
                                <Text style={styles.informationHeadingText}>Type</Text>
                                <View style={styles.typeBox}>
                                    <Text style={styles.typeText}>{SplitCapitalise(restaurantData["type"])}</Text>
                                </View>
                            </View>
                        </View>
                        <View style={[styles.informationContainer, {paddingBottom: '4%'}]}>
                        <View style={styles.leftInformationContainer}>
                                <Text style={[styles.informationHeadingText, {paddingBottom: '3.1%'}]}>Price</Text>
                                <View style={styles.priceLevelDivisor}>
                                    <AntDesign name="creditcard" size={18} color="black"/>
                                    <Text style={[styles.informationContentText, {paddingLeft: '3%'}]}>Medium</Text>
                                </View>
                            </View>
                            <View style={styles.rightInformationContainer}>
                                <Text style={styles.informationHeadingText}>Distance</Text>
                                <Text style={styles.informationContentText}>{distance} Km</Text>
                            </View>
                        </View>
                        <View style={styles.containerBreak}/>
                        <View style={styles.categoryContainer}>
                            <View style={styles.wholeInformationContainer }>
                                <Text style={styles.informationHeadingText}>Establishment Categories</Text>
                                <View style={styles.priceLevelDivisor}>
                                {/* Loop through the restaurant categories to display them */}
                                {restaurantData['categories'].map((category, index) => ( 
                                    <View key={index} style={[styles.typeBox, {marginRight: '3%', marginBottom: '4%'}]} >
                                        <Text style={styles.typeText}>{SplitCapitalise(category)}</Text>
                                    </View>
                                ))}
                                </View>
                            </View>
                        </View>
                        <View style={styles.containerBreak}/>
                        <View style={styles.timeContainer}>
                            <View style={styles.wholeInformationContainer}>
                                {/* For each opening and closing time pass them into the previous function to make it readable */}
                                <Text style={styles.informationHeadingText}>Establishment Hours</Text>
                                    <View style={styles.hoursDivisor}>
                                        <Text style={styles.hoursDay}>
                                            Monday
                                        </Text>
                                        <Text style={styles.hoursTime}>
                                            {getOpeningTime(restaurantData["hours"]["monday"])}
                                        </Text>
                                    </View>
                                    <View style={styles.hoursDivisor}>
                                        <Text style={styles.hoursDay}>
                                            Tuesday
                                        </Text>
                                        <Text style={styles.hoursTime}>
                                            {getOpeningTime(restaurantData["hours"]["tuesday"])}
                                        </Text>
                                    </View>
                                    <View style={styles.hoursDivisor}>
                                        <Text style={styles.hoursDay}>
                                            Wednesday
                                        </Text>
                                        <Text style={styles.hoursTime}>
                                            {getOpeningTime(restaurantData["hours"]["wednesday"])}
                                        </Text>
                                    </View>
                                    <View style={styles.hoursDivisor}>
                                        <Text style={styles.hoursDay}>
                                            Thursday
                                        </Text>
                                        <Text style={styles.hoursTime}>
                                            {getOpeningTime(restaurantData["hours"]["thursday"])}
                                        </Text>
                                    </View>
                                    <View style={styles.hoursDivisor}>
                                        <Text style={styles.hoursDay}>
                                            Friday
                                        </Text>
                                        <Text style={styles.hoursTime}>
                                            {getOpeningTime(restaurantData["hours"]["friday"])}
                                        </Text>
                                    </View>
                                    <View style={styles.hoursDivisor}>
                                        <Text style={styles.hoursDay}>
                                            Saturday
                                        </Text>
                                        <Text style={styles.hoursTime}>
                                            {getOpeningTime(restaurantData["hours"]["saturday"])}
                                        </Text>
                                    </View>
                                    <View style={styles.hoursDivisor}>
                                        <Text style={styles.hoursDay}>
                                            Sunday
                                        </Text>
                                        <Text style={styles.hoursTime}>
                                            {getOpeningTime(restaurantData["hours"]["sunday"])}
                                        </Text>
                                    </View>
                            </View>
                        </View>
                        <View style={styles.containerBreak}/>
                        <View style={styles.categoryContainer}>
                            <View style={styles.wholeInformationContainer}>
                                <Text style={styles.informationHeadingText}>Establishment Attributes</Text>
                                <View style={styles.priceLevelDivisor}>
                                {/* Loop through the restaurant attributes */}
                                { restaurantData["allows_dogs"] == true ?
                                <View style={[styles.typeBox, {marginRight: '3%', marginBottom: '4%'}]} >
                                    <Text style={styles.typeText}>Allows Dogs</Text>
                                </View>
                                :
                                <View/>
                                }
                                { restaurantData["dine_in"] == true ?
                                <View style={[styles.typeBox, {marginRight: '3%', marginBottom: '4%'}]} >
                                    <Text style={styles.typeText}>Dine in</Text>
                                </View>
                                :
                                <View/>
                                }
                                { restaurantData["delivery"] == true ?
                                <View style={[styles.typeBox, {marginRight: '3%', marginBottom: '4%'}]} >
                                    <Text style={styles.typeText}>Delivery</Text>
                                </View>
                                :
                                <View/>
                                }
                                { restaurantData["good_for_children"] == true ?
                                <View style={[styles.typeBox, {marginRight: '3%', marginBottom: '4%'}]} >
                                    <Text style={styles.typeText}>Good for Children</Text>
                                </View>
                                :
                                <View/>
                                }
                                { restaurantData["good_for_groups"] == true ?
                                <View style={[styles.typeBox, {marginRight: '3%', marginBottom: '4%'}]} >
                                    <Text style={styles.typeText}>Good for Groups</Text>
                                </View>
                                :
                                <View/>
                                }
                                { restaurantData["outdoor_seating"] == true ?
                                <View style={[styles.typeBox, {marginRight: '3%', marginBottom: '4%'}]} >
                                    <Text style={styles.typeText}>Outdoor Seating</Text>
                                </View>
                                :
                                <View/>
                                }
                                </View>
                            </View>
                        </View>
                        <View style={styles.containerBreak}/>
                        <View style={[styles.categoryContainer, {marginBottom: '2%'}]}>
                            <View style={styles.wholeInformationContainer}>
                                <Text style={styles.informationHeadingText}>Similar Establishments</Text>
                            </View>
                        </View>
                        {restaurantRecommendationData.map(item => (
                            <RestaurantCard key={item.id} restaurantData={item} />
                        ))}
                        <View style={styles.containerBreak}/>
                        <View style={styles.categoryContainer}>
                            <View style={styles.wholeInformationContainer}>
                                <Text style={styles.informationHeadingText}>Establishments Reviews</Text>
                            </View>
                        </View>
                        <View style={styles.topNavBar} >
                    { selectedReviews == "positive" ? 
                        <TouchableOpacity style={styles.navBarContentSelected} onPress={() => {  }}>
                            <Text style={styles.topNavBarTextSelected}>
                                Positive
                            </Text>
                        </TouchableOpacity>
                        :
                        <TouchableOpacity style={styles.navBarContent} onPress={() => { setSelectedReviews("positive") }}>
                            <Text style={styles.topNavBarText}>
                                Positive
                            </Text>
                        </TouchableOpacity>
                    }
                    { selectedReviews == "all" ? 
                        <TouchableOpacity style={styles.navBarContentSelected} onPress={() => {  }}>
                            <Text style={styles.topNavBarTextSelected}>
                                All
                            </Text>
                        </TouchableOpacity>
                        :
                        <TouchableOpacity style={styles.navBarContent} onPress={() => { setSelectedReviews("all") }}>
                            <Text style={styles.topNavBarText}>
                                All
                            </Text>
                        </TouchableOpacity>
                    }
                    { selectedReviews == "negative" ? 
                        <TouchableOpacity style={styles.navBarContentSelected} onPress={() => {  }}>
                            <Text style={styles.topNavBarTextSelected}>
                                Negative
                            </Text>
                        </TouchableOpacity>
                        :
                        <TouchableOpacity style={styles.navBarContent} onPress={() => { setSelectedReviews("negative") }}>
                            <Text style={styles.topNavBarText}>
                                Negative
                            </Text>
                        </TouchableOpacity>
                    }        
                </View>
                <View style={styles.headingContainer}>
                    <Text style={styles.establishmentNumber}>{data.length} Reviews</Text> 
                    {/* When clicked the modal for sorting appears */}
                    <TouchableOpacity style={styles.sortByContainer} onPress={() => changeSort()}>
                        <Text style={styles.establishmentSortBy} > {sortVisual} </Text>
                        <AntDesign name="caretdown" size={12} color='#1C58F2' style={{paddingTop: "1%", paddingLeft: "1%"}}/>
                    </TouchableOpacity>
                    <ReviewSortBy visible={modalSortVisible} onClose={() => setModalSortVisible(false)} setSortVisual={setSortVisual} />
                </View>                
                <View>
                {/* Loop through the restaurant information so that it is displayed */}
                <ReviewRestaurantList data={data} />
                </View>
                <View style={styles.deadSpace}/>
                <View style={styles.deaderSpace}/>
                </View>
                </ScrollView>
                {/* Clicking the review button will pull up the modal */}
                <TouchableOpacity style={styles.reviewButton} onPress={() => toggleModal()}>
                    <Text style={styles.buttonText}>Review Now</Text>
                    <CreateReviewScreen visible={modalVisible} onClose={() => setModalVisible(false)} id={id} restaurantData={restaurantData} />
                </TouchableOpacity>
                </View>
                }
        </Modal>
    );
};

const styles = StyleSheet.create({
    // main container for the whole screen
    mainContainer: {
        backgroundColor: '#F5F7FC',
        height: '100%',
    },
    // container for the top of the screen
    backContainer: {
        flexDirection: 'row',
        paddingLeft: '10%',
        width: '100%',
        backgroundColor: 'white',
    },
    // title container
    titleContainer: {
        paddingTop: '5%',
        paddingLeft: '10%',
        paddingRight: '10%',
        width: '100%',
        backgroundColor: 'white',
    },
    // restaurant title styling
    restaurantTitleText: {
        fontWeight: '500',
        fontSize: 30,
        color: '#000000'
    },
    // restaurant address container
    addressContainer: {
        paddingTop: '1%',
        paddingLeft: '10%',
        paddingRight: '10%',
        width: '100%',
        backgroundColor: 'white',
        paddingBottom: '4%',
    },
    // restaurant addres styling
    restaurantAddressText: {
        fontWeight: '500',
        fontSize: 16,
        color: '#525357'
    },
    // break between containers
    containerBreak: {
        width: '100%',
        height: 20,
        backgroundColor: '#F5F7FC',
    },
    // information about restaurant container
    informationContainer: {
        paddingTop: '4%',
        width: '100%',
        flexDirection: 'row',
        backgroundColor: 'white',
    },
    // information on left
    leftInformationContainer: {

        width: "50%",
        paddingLeft: "10%",
    },
    // information on right
    rightInformationContainer: {
        width: "50%",
        paddingLeft: "5%",
        paddingRight: '10%',
    },
    // information heading text syling
    informationHeadingText: {
        fontWeight: '700',
        fontSize: 16,
        color: '#525357', 
        paddingBottom: '4%',
    },
    // information content text styling
    informationContentText: {
        fontWeight: '700',
        fontSize: 16,
        color: '#333333'
    },
    // type of restaurant styling
    typeBox: {
        paddingLeft: 7,
        paddingRight: 7,
        paddingBottom: 2,
        paddingTop: 1,
        borderRadius: 50,
        backgroundColor: '#F5F7FC',
        alignItems: 'flex-start',
        alignSelf: 'flex-start',
    },
    // text in the box
    typeText: {
        fontSize: 16,
        color: '#333333',
        fontWeight: '600',
    },
    // price level styling
    priceLevelDivisor: {
        flexDirection: 'row',
        flexWrap: 'wrap'
    },
    // category container styling
    wholeInformationContainer: {
        paddingLeft: '10%',
        paddingRight: '10%',
        width: '100%',
    },
    // category container styling
    categoryContainer: {
        paddingTop: '4%',
        width: '100%',
        backgroundColor: 'white',
    },
    // time container styling
    timeContainer: {
        paddingTop: '4%',
        width: '100%',
        backgroundColor: 'white',
        paddingBottom: '2%',
    },
    // split for hours and day
    hoursDivisor: {
        width: '100%',
        flexDirection: 'row',
        justifyContent: 'space-between',
        backgroundColor: 'white',
    },
    // day styling
    hoursDay: {
        fontSize: 18,
        color: 'black',
        paddingBottom: "2%"
    },
    // time styling
    hoursTime: {
        fontSize: 18,
        color: 'black',
        paddingBottom: "2%",
    },
    // review button styling
    reviewButton: {
        position: 'absolute',
        width: '74%',
        bottom: 110,
        height: '7%',
        backgroundColor: '#1C58F2',
        left: '13%',
        borderRadius: 20,

        justifyContent: 'center',
        alignItems: 'center',
    },
    // text in button
    buttonText: {
        textAlign: 'center',
        fontSize: 25,
        fontWeight: '600',
        color: 'white'
    },
    deadSpace: {
        height: 200,
        backgroundColor: '#F5F7FC',
    },
    deaderSpace: {
        height: "40%",
        backgroundColor: '#F5F7FC',
    },
    // top nav bar styling
    topNavBar: {
        marginLeft: '10%',
        marginRight: '10%',
        borderRadius: 20000,
        height: 50,
        flexDirection: 'row', 
    },
    // content in the nav bar
    navBarContent: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    // selected parts of the nav bar
    navBarContentSelected: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#1C58F2',
        borderRadius: 20000,
    },
    // top nav bar text
    topNavBarText: {
        fontWeight: '700',
        fontSize: 17,
        color: 'black',
    },
    // top nav bar text for selected 
    topNavBarTextSelected: {
        fontWeight: '700',
        fontSize: 17,
        color: 'white',
    },
    headingContainer: {
        paddingTop: '5%',
        paddingLeft: '5%',
        paddingRight: '5%',
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    // Styling for the establishment text
    establishmentNumber: {
        fontWeight: '700',
        fontSize: 16,
        color: '#525357',
    },
    // Styling for the sort by container
    sortByContainer: {
        flexDirection: 'row',
    },
    // Styling for the establishment sort by text
    establishmentSortBy: {
        fontWeight: '700',
        fontSize: 16,
        color: '#1C58F2', //333333
    },
});

export default IndividualRestaurantModal;