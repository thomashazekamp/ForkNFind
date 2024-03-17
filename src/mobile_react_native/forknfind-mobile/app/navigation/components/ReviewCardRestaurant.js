import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import EditReviewScreen from './EditReviewScreen';

// Functional Component ReviewCardRestaurant
// data - passed in review information
const ReviewCardRestaurant = ( {data} ) => {

    // Use states for updating the page when new information is came across
    const [starOne, setStarOne] = useState(true);
    const [starTwo, setStarTwo] = useState(false);
    const [starThree, setStarThree] = useState(false);
    const [starFour, setStarFour] = useState(false);
    const [starFive, setStarFive] = useState(false);

    const {
        rating,
        description,
    } = data;

    // use effect on startup to check how many stars are needed
    useEffect(() => {
        
        if (rating == 1) {
            setStarOne(true)
            setStarTwo(false)
            setStarThree(false)
            setStarFour(false)
            setStarFive(false)
        } else if (rating == 2) {
            setStarOne(true)
            setStarTwo(true)
            setStarThree(false)
            setStarFour(false)
            setStarFive(false)
        } else if (rating == 3) {
            setStarOne(true)
            setStarTwo(true)
            setStarThree(true)
            setStarFour(false)
            setStarFive(false)
        } else if (rating == 4) {
            setStarOne(true)
            setStarTwo(true)
            setStarThree(true)
            setStarFour(true)
            setStarFive(false)
        } else if (rating == 5) {
            setStarOne(true)
            setStarTwo(true)
            setStarThree(true)
            setStarFour(true)
            setStarFive(true)
        }
    }, []);

    return (
        // surround the card in a touchable component
        <View style={styles.container}>
            <Text style={styles.restaurantName}>{data["restaurant"].name}</Text>
            <View style={styles.rowContainer}>
                <View style={styles.starContainer}>
                    <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                        { starOne ? (<AntDesign name="star" size={25} color="#DBFF00" style={{position: 'absolute'}}/>) : (<View/>)}
                        <AntDesign name="staro" size={25} color="#000000" style={{position: 'absolute'}}/>
                    </View>
                    <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                        { starTwo ? (<AntDesign name="star" size={25} color="#DBFF00" style={{position: 'absolute'}}/>) : (<View/>)}
                        <AntDesign name="staro" size={25} color="#000000" style={{position: 'absolute'}}/>
                    </View>
                    <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                        { starThree ? (<AntDesign name="star" size={25} color="#DBFF00" style={{position: 'absolute'}}/>) : (<View/>)}
                        <AntDesign name="staro" size={25} color="#000000" style={{position: 'absolute'}}/>
                    </View>
                    <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                        { starFour ? (<AntDesign name="star" size={25} color="#DBFF00" style={{position: 'absolute'}}/>) : (<View/>)}
                        <AntDesign name="staro" size={25} color="#000000" style={{position: 'absolute'}}/>
                    </View>
                    <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                        { starFive ? (<AntDesign name="star" size={25} color="#DBFF00" style={{position: 'absolute'}}/>) : (<View/>)} 
                        <AntDesign name="staro" size={25} color="#000000" style={{position: 'absolute'}}/>
                    </View>
                </View>
                <Text style={styles.dateText}>
                    {data["date"]}
                </Text>
            </View>
            <View style={styles.descriptionContainer}>
                <Text>{description}</Text>
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    // container card styling
    container: {
        width: '90%',
        left: '5%',
        right: '5%',
        marginTop: '2.5%',
        marginBottom: '2.5%',
        backgroundColor: 'white',
        borderRadius: 20
    },
    // restaurant name styling
    restaurantName: {
        paddingTop: '5%',
        paddingLeft: '7.5%',
        fontSize: 18,
        fontWeight: 'bold',
        color: '#181A1F'
    },
    // star container styling
    starContainer: {
        paddingTop: '4%',
        marginLeft: '7%',
        width: '35%',
        backgroundColor: 'white',
        flexDirection: 'row',
        paddingBottom: '12%',
    },
    // spacing between stars
    starSection: {
        width: '20%',
    },
    // row split
    rowContainer: {
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    // data text styling
    dateText: {
        paddingRight: '7.5%',
        fontWeight: '700',
        fontSize: 16,
        color: '#525357',
        paddingTop: '1.8%',
    },
    // description styling
    descriptionContainer: {
        marginTop: "-5%",
        paddingLeft: '7.5%',
        paddingRight: '7.5%',
        paddingBottom: "5%"
    }
});

export default ReviewCardRestaurant;