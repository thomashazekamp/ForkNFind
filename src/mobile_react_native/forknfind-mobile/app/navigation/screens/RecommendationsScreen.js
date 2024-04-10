import React, { useState, useEffect} from 'react';
import { View, Text, TouchableOpacity, StyleSheet, StatusBar, ActivityIndicator, Dimensions, RefreshControl } from 'react-native';

import { AntDesign } from '@expo/vector-icons';
import { ScrollView } from 'react-native-gesture-handler';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useFocusEffect } from '@react-navigation/native';

import RestaurantCard from '../components/RestaurantCard';
import HybridRecommendationsAPIRequest from '../requests/HybridRecommendationsAPIRequest';
import RestaurantSortBy from '../components/RestaurantSortBy';

// Functional Component RecommendationsScreen
// navigation - used to link to other screens created
export default function RecommendationsScreen({ navigation }) {

    // Use states for updating the page when new information is came across
    const [screenDimensions, setScreenDimensions] = useState(Dimensions.get('window'));
    const [data, setData] = useState(null);
    const [originalData, setOriginalData] = useState(data);
    const [modalSortVisible, setModalSortVisible] = useState(false);
    const [sortVisual, setSortVisual] = useState("All Relevance");
    const [userReload, setUserReload] = useState(false)

    // On startup query the API to get the recommendation information
    useEffect(() => {
        HybridRecommendationsAPIRequest(setData, setOriginalData);
    }, []);

    // If the sort button is hit get the modal visible
    const changeSort = () => {

        setModalSortVisible(!modalSortVisible);
    }

    useFocusEffect(() => {
        StatusBar.setBarStyle('dark-content')
    });

    // Use effect called when the sort has been updated
    useEffect(() => {

        // Depending on which was selected update the data to be sorted in that way
        if (sortVisual == "All Relevance") {

            setData(originalData)
        } else if (sortVisual == "Ratings (Ascending)") {
    
            // Sort the data such that the lowest ratings are first and gradually getting higher
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

    useEffect(() => {
        if (userReload == true) {
            setData(null)
            HybridRecommendationsAPIRequest(setData, setOriginalData);
            setUserReload(false)
        }
    }, [userReload]);
    
    return (
        <View style={{flex: 1, backgroundColor: '#F5F7FC'}}>
        <SafeAreaView style={styles.container}/>
            <StatusBar barStyle="dark-content" />
            <ScrollView style={styles.containerScrollView} refreshControl={ <RefreshControl onRefresh={() => { setUserReload(true)  }} tintColor="transparent" colors={['transparent']} />}> 
                {data == null ? 
                    <View style={{
                        width: '100%',
                        height: (screenDimensions.height - 200),
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
                        <Text style={styles.establishmentNumber}>{data.length} Establishments</Text> 
                        {/* When clicked the modal for sorting appears */}
                        <TouchableOpacity style={styles.sortByContainer} onPress={() => changeSort()}>
                            <Text style={styles.establishmentSortBy} > {sortVisual} </Text>
                            <AntDesign name="caretdown" size={12} color='#1C58F2' style={{paddingTop: "1%", paddingLeft: "1%"}}/>
                        </TouchableOpacity>
                        <RestaurantSortBy visible={modalSortVisible} onClose={() => setModalSortVisible(false)} setSortVisual={setSortVisual} />
                    </View>                
                    <View>
                    {/* Loop through the restaurant information so that it is displayed */}
                    {data.map(item => (
                        <RestaurantCard key={item.id} restaurantData={item} />
                    ))}
                    </View>
                </View>
                }
                <View style={styles.deadSpace}/>
                <View style={styles.deaderSpace}/>
            </ScrollView>
        </View>
        
    );
};

const styles = StyleSheet.create({
    // Screen styling
    container: {
        flex: 1,
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
    sortByContainer: {
        flexDirection: 'row',
    },
    // Styling for the establishment sort by text
    establishmentSortBy: {
        fontWeight: '700',
        fontSize: 16,
        color: '#1C58F2',
    },
});