import React, { useState, useEffect} from 'react';
import { View, Text, TouchableOpacity, StyleSheet, StatusBar, ActivityIndicator, Dimensions, RefreshControl } from 'react-native';

import { AntDesign } from '@expo/vector-icons';
import { ScrollView } from 'react-native-gesture-handler';
import { SafeAreaView } from 'react-native-safe-area-context';

import GetAllUserReviews from '../requests/GetAllUserReviews';
import ReviewSortBy from '../components/ReviewSortBy';
import ReviewList from '../components/ReviewList';

// Functional Component ReviewScreen
// navigation - used to link to other screens created
export default function ReviewScreen({ navigation }) {

    // Use states for updating the page when new information is came across
    const [screenDimensions, setScreenDimensions] = useState(Dimensions.get('window'));
    const [data, setData] = useState(null);
    const [originalData, setOriginalData] = useState(data);
    const [selectedReviews, setSelectedReviews] = useState("all");
    const [modalSortVisible, setModalSortVisible] = useState(false);
    const [sortVisual, setSortVisual] = useState("All Relevance");
    const [reload, setReload] = useState(false)
    const [userReload, setUserReload] = useState(false)

    // On startup query the API to get the recommendation information
    useEffect(() => {
        GetAllUserReviews(setData, setOriginalData);
    }, []);

    useEffect(() => {
        if (reload == true) {
            setData(null)
            GetAllUserReviews(setData, setOriginalData);
            setReload(false)
        }
    }, [reload]);

    useEffect(() => {
        if (userReload == true) {
            setData(null)
            GetAllUserReviews(setData, setOriginalData);
            setUserReload(false)
        }
    }, [userReload]);

    // If the sort button is hit get the modal visible
    const changeSort = () => {

        setModalSortVisible(!modalSortVisible);
    }

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
    
    return (
        <View style={{backgroundColor: '#F5F7FC', flex: 1}}>
        <SafeAreaView style={styles.container}/>
            <StatusBar barStyle="dark-content" />
            <ScrollView style={styles.containerScrollView} refreshControl={ <RefreshControl onRefresh={() => { setUserReload(true)  }} tintColor="transparent" colors={['transparent']} />} >
                {/* Top nav abr code allowing for switch between different types of reviews */}
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
                {data == null ? 
                    <View style={{
                        width: '100%',
                        height: (screenDimensions.height - 300),
                    }}> 
                        <ActivityIndicator size="large" color="#1C58F2" style={{
                        flex: 1,
                        alignItems: 'center',
                        justifyContent: 'center', 
                    }} />
                    </View>
                    :
                    <View>
                        <View style={styles.headingContainer}>
                            <Text style={styles.establishmentNumber}> {data.length} Reviews</Text> 
                            {/* When clicked the modal for sorting appears */}
                            <TouchableOpacity style={styles.sortByContainer} onPress={() => changeSort()}>
                                <Text style={styles.establishmentSortBy} > {sortVisual} </Text>
                                <AntDesign name="caretdown" size={12} color='#1C58F2' style={{paddingTop: "1%", paddingLeft: "1%"}}/>
                            </TouchableOpacity>
                            <ReviewSortBy visible={modalSortVisible} onClose={() => setModalSortVisible(false)} setSortVisual={setSortVisual} />
                        </View>
                        {/* ReviewtList is wrapped in React Memo such that it will only reload when the data changes */}
                        <ReviewList data={data} setReload={setReload} />
                    </View>
                    }
                <View style={styles.deadSpace}/>
                <View style={styles.deaderSpace}/>
            </ScrollView>
        </View> 
    );
};

const styles = StyleSheet.create({
    // screen styling
    container: {
        backgroundColor: '#F5F7FC'
    },
    // Scroll view styling
    containerScrollView: {
        paddingLeft: 10,
        paddingRight: 10,
    },
    // Dead space so that while scrolling you see the correct colour
    deadSpace: {
        height: 200,
        backgroundColor: '#F5F7FC',
    },
    deaderSpace: {
        height: "40%",
        backgroundColor: '#F5F7FC',
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
    }
});