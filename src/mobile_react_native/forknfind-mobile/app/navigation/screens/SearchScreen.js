/* 
-----------------
Reference: https://www.youtube.com/watch?v=Q4S9M9rJAxk&ab_channel=PradipDebnath
           - This video was used as a reference for the search functionality (not the filtering of the search)
           https://www.youtube.com/watch?v=YwwX0DiAvCQ&ab_channel=CodewithBeto
           - This video was used as a reference for the filtering of the search, adapting it to my own code
-----------------
*/

import React, { useState, useRef, useEffect } from 'react';
import { View, Text, StyleSheet, TextInput, SafeAreaView, StatusBar, ScrollView, TouchableOpacity } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { FontAwesome } from '@expo/vector-icons';
import { Ionicons } from '@expo/vector-icons';
import { AntDesign } from  '@expo/vector-icons';
import RestaurantCard from '../components/RestaurantCard';
import FilterScreen from '../components/FilterScreen';
import SearchAPIRequest from '../requests/SearchAPIRequest'
import RestaurantSortBy from '../components/RestaurantSortBy';

// Functional Component SearchScreen
// navigation - used to link to other screens created
export default function SearchScreen({ navigation }) {

    // Use states for updating the page when new information is came across
    const [data, setData] = useState([]);
    const [modalVisible, setModalVisible] = useState(false);
    const [originalData, setOriginalData] = useState(data);
    const [modalSortVisible, setModalSortVisible] = useState(false);
    const [sortVisual, setSortVisual] = useState("All Relevance");
    const [location, setLocation] = useState(null);

    // Saving potiential filter information
    const searchQueryRef = useRef({
        "name" : '',
        "address" : '',
        "categories" : '',
        "attributes" : '',
        "allows_dogs" : false,
        "delivery" : false,
        "dine_in" : false,
        "good_for_children" : false,
        "good_for_groups" : false,
        "outdoor_seating" : false,
    });

    // Update the search name
    const refSearchUpdate = (text) => {
        searchQueryRef.current.name = text;
    };

    // Search request
    const searchItem = () => {
        SearchAPIRequest(searchQueryRef, setData, setOriginalData, location)
    }

    // Sort screen
    const changeSort = () => {

        setModalSortVisible(!modalSortVisible);
    }

    // On startup get the location from async storage
    useEffect(() => {

        const retrieveLocation = async () => {
            try {
                const latitude = await AsyncStorage.getItem('locationDataLatitude');
                const longitude = await AsyncStorage.getItem('locationDataLongitude');
                if (latitude !== null && longitude !== null) {
                    console.log(latitude, longitude)
                    return {latitude, longitude}
                }
                } catch (error) {
                    console.log(error)
            }
        }
    
        const fetchLocationData = async () => {
            const locationData = await retrieveLocation();
            setLocation(locationData);
        };
        
        fetchLocationData();
        
    }, []);

    // Use effect when sorting has been updated
    useEffect(() => {

        if (sortVisual == "All Relevance") {

            setData(originalData)
        } else if (sortVisual == "Ratings (Ascending)") {
    
            const array = Object.values(data);
            array.sort((a, b) => a.average_rating - b.average_rating);
            setData(array)
    
        } else if (sortVisual == "Ratings (Descending)") {
    
            const array = Object.values(data);
            array.sort((a, b) => b.average_rating - a.average_rating);
            setData(array)

        } else if (sortVisual == "Alphabetical (A - Z)") {
    
            const array = Object.values(data);
            array.sort((a, b) => a.name.localeCompare(b.name));
            setData(array);
        } else if (sortVisual == "Alphabetical (Z - A)") {
    
            const array = Object.values(data);
            array.sort((a, b) => b.name.localeCompare(a.name));
            setData(array);
        } else if (sortVisual == "Distance (Ascending)") {
    
            const array = Object.values(data);
            array.sort((a, b) => a.distance_from_user - b.distance_from_user);
            setData(array)
        } else if (sortVisual == "Distance (Descending)") {
    
            const array = Object.values(data);
            array.sort((a, b) => b.distance_from_user - a.distance_from_user);
            setData(array)
        }
    }, [sortVisual]);

    // toggling modal
    const toggleModal = () => {
        setModalVisible(!modalVisible);
    }
    
    return (
        <View style={{backgroundColor: '#F5F7FC'}}>
        <SafeAreaView style={styles.container}/>
            <StatusBar barStyle="dark-content" />
            <ScrollView style={styles.containerScrollView}>
            {/* Search box holding 2 icons and text box */}
            <View style={styles.textBox}>
                <FontAwesome name="search" size={22} color="white" onPress={() => searchItem()}/>
                <TextInput 
                    placeholder="Search"
                    placeholderTextColor="white"
                    style={styles.searchBox}
                    autoCapitalize='none'
                    autoCorrect={false}
                    onChangeText={refSearchUpdate}
                />
                <TouchableOpacity onPress={() => toggleModal({})}>
                    <Ionicons name="filter-sharp" size={22} color="white"/>
                </TouchableOpacity>
                <FilterScreen visible={modalVisible} onClose={() => setModalVisible(false)} searchQueryRef={searchQueryRef} />
            </View>
            <View style={styles.headingContainer}>
                    <Text style={styles.establishmentNumber}>{data.length} Establishments</Text> 
                    <TouchableOpacity style={styles.sortByContainer} onPress={() => changeSort()}>
                        <Text style={styles.establishmentSortBy} > {sortVisual} </Text>
                        <AntDesign name="caretdown" size={12} color='#1C58F2' style={{paddingTop: "1%", paddingLeft: "1%"}}/>
                    </TouchableOpacity>
                    <RestaurantSortBy visible={modalSortVisible} onClose={() => setModalSortVisible(false)} setSortVisual={setSortVisual} />
            </View>
            <View>
                {/* Looping through results from search */}
                {data.map(item => (
                    <RestaurantCard key={item.id} restaurantData={item} />
                ))}
            </View>
            <View style={styles.deadSpace}/>
            </ScrollView>
            <View style={styles.deaderSpace}/>
        </View>
    );
}

const styles = StyleSheet.create ({
    // Screen container
    container: {
        flex: 1,
        backgroundColor: '#F5F7FC'
    },
    // scroll view styling
    containerScrollView: {
        paddingLeft: 10,
        paddingRight: 10,
    },
    // search box styling
    searchBox: {
        backgroundColor: '#1C58F2',
        fontSize: 17,
        fontWeight: '500',
        flex: 1, 
        marginLeft: 15, 
        color: 'white',
    },
    // text box within styling
    textBox: {
        marginLeft: '5%',
        marginRight: '5%',
        flexDirection: 'row', 
        justifyContent: 'space-between',
        backgroundColor: '#1C58F2',
        color: 'white',
        paddingHorizontal: 20,
        paddingVertical: 16,
        marginTop: 25,
        borderRadius: 18,
        fontSize: 16,
        fontWeight: '500',
    },
    // Dead space so that while scrolling you see the correct colour
    deadSpace: {
        height: 180,
        backgroundColor: '#F5F7FC',
    },
    deaderSpace: {
        height: 1000,
        backgroundColor: '#F5F7FC',
    },
    // Container heading
    headingContainer: {
        paddingTop: '5%',
        paddingLeft: '5%',
        paddingRight: '5%',
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    // styling for establishment
    establishmentNumber: {
        fontWeight: '700',
        fontSize: 16,
        color: '#525357', 
    },
    // styling for sort
    sortByContainer: {
        flexDirection: 'row',
    },
    // sort text styling
    establishmentSortBy: {
        fontWeight: '700',
        fontSize: 16,
        color: '#1C58F2',
    },
    
})