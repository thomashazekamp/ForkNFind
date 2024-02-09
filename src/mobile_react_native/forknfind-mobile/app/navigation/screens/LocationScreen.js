import React, { useState, useEffect } from 'react';
import { View, StyleSheet, StatusBar, Image, ActivityIndicator, TouchableOpacity } from 'react-native';
import { Marker, Callout } from 'react-native-maps';
import MapView from "react-native-map-clustering";

import * as Location from 'expo-location';

import NearbyRestaurantsAPIRequest from '../requests/NearbyRestaurantsAPIRequest';
import RestaurantCardMap from '../components/RestaurantCardMap';
import AsyncStorage from '@react-native-async-storage/async-storage';
import MapFilter from '../components/MapFilter';
import { MaterialIcons } from '@expo/vector-icons';

// Functional Component LoginScreen
// navigation - used to link to other screens created
export default function LocationScreen({ navigation }) {

    // Use states to manage the information
    const [deviceLocation, setDeviceLocation] = useState(null);
    const [data, setData] = useState(null)

    const [originalData, setOriginalData] = useState(null);
    const [modalSortVisible, setModalSortVisible] = useState(false);
    const [sortVisual, setSortVisual] = useState("All");

    // Reference: https://stackoverflow.com/questions/68955119/react-native-expo-location-returns-location-service-unavailable-during-initial-u
    // Response by user Dharman, Aug 27th 2021
    // This code was adapted from a solution found online on stack overflow
    useEffect(() => {
        (async () => {
        const { status } = await Location.requestForegroundPermissionsAsync();
        if (status === 'granted') {
            const locationData = await Location.getCurrentPositionAsync({});
            setDeviceLocation(locationData);
            saveLocationData(locationData)

            NearbyRestaurantsAPIRequest(setData, locationData, setOriginalData);

        }
        })();
    }, []);

    const saveLocationData = async (locationData) => {
        try {
            await AsyncStorage.setItem(
                "locationDataLongitude", String(locationData['coords']['longitude'])
            )
            await AsyncStorage.setItem(
                "locationDataLatitude", String(locationData['coords']['latitude'])
            )
        } catch (error) {
            console.log(error)
        }
    }

    const changeSort = () => {

        setModalSortVisible(!modalSortVisible);
    }

    useEffect(() => {

        if (sortVisual == "All") {

            setData(originalData)
        } else if (sortVisual == "Open") {

            const array = Object.values(originalData);
            const filteredArray = array.filter(item => item.open_or_close === "Open");
            setData(filteredArray)

        } else if (sortVisual == "Closed") {

            const array = Object.values(originalData);
            const filteredArray = array.filter(item => item.open_or_close === "Closed");
            setData(filteredArray)

        } else if (sortVisual == "Recommended") {

            const array = Object.values(originalData);
            const filteredArray = array.filter(item => item.recommend === true);
            setData(filteredArray)
        }
    }, [sortVisual]);

    return (
        // Map view code using React library
        <View style={styles.container}>
            <StatusBar barStyle="light-content" />
                {data !== null ? 
                <View style={styles.container}>
                    <MapView
                        style={styles.map}
                        initialRegion={{
                            latitude: deviceLocation["coords"]["latitude"],
                            longitude: deviceLocation["coords"]["longitude"],
                            latitudeDelta: 0.045,
                            longitudeDelta: 0.02,
                    }}
                        showsPointsOfInterest={false}
                    >
                        {/* Mark user location */}
                        <Marker
                            coordinate={{
                            latitude: deviceLocation["coords"]["latitude"],
                            longitude: deviceLocation["coords"]["longitude"],
                            }}
                            title="Your Location"
                        >
                            <Image
                                source={require('../../../image/user_icon.png')}
                                style={{width: 33, height:48, marginBottom: 40}}
                            />
                        </Marker>
                        {/* Mark the restaurant locations by looping through data */}
                        {Object.keys(data).map(key => ( 
                        <Marker key={key} coordinate={{ latitude: data[key]["location"][1], longitude: data[key]["location"][0]}} >
                            { data[key]["open_or_close"] == "Open" ?
                            ( data[key]["recommend"] == true ?
                                <Image
                                    source={require('../../../image/recommend_marker.png')}
                                    style={{width: 33, height:48, marginBottom: 40}}
                                />
                                :
                                <Image
                                    source={require('../../../image/open_marker.png')}
                                    style={{width: 33, height:48, marginBottom: 40}}
                                />
                            )
                            :
                            ( data[key]["recommend"] == true ?
                                <Image
                                    source={require('../../../image/recommend_marker.png')}
                                    style={{width: 33, height:48, marginBottom: 40}}
                                />
                            :
                                <Image
                                    source={require('../../../image/closed_marker.png')}
                                    style={{width: 33, height:48, marginBottom: 40}}
                                />
                            )
                            }
                            <Callout tooltip={true}>
                                <RestaurantCardMap restaurantData={data[key]} />
                            </Callout>
                        </Marker> ))}
                    </MapView>
                    <TouchableOpacity onPress={() => changeSort()} style={styles.buttonContainer}>
                        <MaterialIcons name="location-pin" size={40} color="white" />
                    </TouchableOpacity>
                    <MapFilter visible={modalSortVisible} onClose={() => setModalSortVisible(false)} setSortVisual={setSortVisual} />
                </View>
                :
                <View style={{
                    flex: 1, 
                    alignItems: 'center',
                    justifyContent: 'center', 
                }}> 
                <ActivityIndicator size="large" color="#1C58F2" />
                </View>
                }
        </View>
    );
}

/* <Image source={require('../../../image/custom_marker.png')} style={{ width: 50, height: 50 }}/> */
const styles = StyleSheet.create({
    // Container takig the whole screen
    container: {
        ...StyleSheet.absoluteFillObject,
        flex: 1,
        justifyContent: 'flex-end',
        alignItems: 'center',
        backgroundColor: '#F5F7FC'
    },
    // map taking up all the space
    map: {
        ...StyleSheet.absoluteFillObject,
    },
    buttonContainer: {
        position: 'absolute',
        right: 20,
        bottom: 140,
        height: 70,
        width: 70,
        backgroundColor: '#407BFF',
        borderRadius: 500,
        justifyContent: 'center',
        alignItems: 'center',
    }
});