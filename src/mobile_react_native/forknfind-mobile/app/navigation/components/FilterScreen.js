import React, { useState } from 'react';
import { View, Text, StyleSheet, Modal, TouchableOpacity, SafeAreaView, StatusBar, KeyboardAvoidingView } from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { ScrollView, TextInput } from 'react-native-gesture-handler';
import CategoryFilter from './CategoryFilter';

// Functional Component SearchScreen
// visible - whether modal is visible or not
// onClose - how to close screen
// searchQueryRef - search query input
const FilterScreen = ({ visible, onClose, searchQueryRef}) => {

    // Use states of all the possible changes
    const [radioButton, setRadioButton] = useState(1);
    const [allowsDogs, setAllowsDogs] = useState(false);
    const [goodForChildren, setGoodForChildren] = useState(false);
    const [dineIn, setDineIn] = useState(false);
    const [goodForGroups, setGoodForGroups] = useState(false);
    const [outdoorSeating, setOutdoorSeating] = useState(false);
    const [delivery, setDelivery] = useState(false);
    const [addressValue, setAddressValue] = useState('')
    const [nameValue, setNameValue] = useState('')
    const [selectedCategories, setSelectedCategories] = useState([]);

    // Updating the name value in text box
    const nameSearchUpdate = (text) => {
        setNameValue(text);
    };

    // Updating the address value in text box
    const addressSearchUpdate = (text) => {
        setAddressValue(text); 
    }

    // When save filter is pressed save all the value
    const saveFilter = () => {

        searchQueryRef.current.name =  nameValue;
        searchQueryRef.current.address = addressValue;
        // set average rating to 0 to prevent issues
        searchQueryRef.current.average_rating = 0;
        searchQueryRef.current.categories = selectedCategories

        if (allowsDogs == true) {
            searchQueryRef.current.allows_dogs = true
        }
        if (goodForChildren == true) {
            searchQueryRef.current.good_for_children = true
        }
        if (goodForGroups == true) {
            searchQueryRef.current.good_for_groups = true
        }
        if (dineIn == true) {
            searchQueryRef.current.dine_in = true
        }
        if (delivery == true) {
            searchQueryRef.current.delivery = true
        }
        if (outdoorSeating == true) {
            searchQueryRef.current.outdoor_seating = true
        }

        onClose();
    }

    // If reset is clicked then reset all states
    const resetFilter = () => {

        setRadioButton(1);
        setAllowsDogs(false);
        setGoodForChildren(false);
        setDineIn(false);
        setGoodForGroups(false);
        setOutdoorSeating(false);
        setDelivery(false);
        setAddressValue("");
        setNameValue("");
        setSelectedCategories([]);
    }

    return (
        <Modal
        animationType="slide"
        transparent={false}
        visible={visible}
        onRequestClose={onClose}
    >
        <StatusBar barStyle="dark-content" />
        <SafeAreaView style={{ backgroundColor: "white" }} />
        {/* Prevent keyboards from blocking view */}
        <KeyboardAvoidingView
            behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
        >
        <ScrollView>
            <View style={styles.mainContainer}>
                    <View style={styles.backContainer}>
                        <TouchableOpacity onPress={() => { onClose(); resetFilter()}}>
                            <AntDesign name="arrowleft"  size={28} color={"black"} style={{paddingTop: '5%'}}/>
                        </TouchableOpacity>
                    </View>
                    <View style={[styles.textContainer]}>
                        <Text style={styles.ratingHeadingText}>Name</Text>
                        <TextInput 
                            placeholder="Name"
                            placeholderTextColor="black"
                            autoCapitalize='none'
                            style={styles.textBox}
                            autoCorrect={false}
                            onChangeText={nameSearchUpdate}
                            value={nameValue}
                            >
                        </TextInput>  
                    </View>
                    <View style={[styles.textContainer, {paddingTop: "0%"}]}>
                        <Text style={styles.ratingHeadingText}>Address</Text>
                        <TextInput 
                            placeholder="Address"
                            placeholderTextColor="black"
                            autoCapitalize='none'
                            style={styles.textBox}
                            autoCorrect={false}
                            onChangeText={addressSearchUpdate}
                            value={addressValue}
                            >
                        </TextInput>  
                    </View>
                    <View style={styles.containerBreak}/>
                    <View style={[styles.textContainer]}>
                        <Text style={styles.ratingHeadingText}>Rating</Text>
                        <View style={styles.starLineContainer}>
                            <View style={styles.starContainer}>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="star" size={30} color="#DBFF00" style={{position: 'absolute'}}/>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="star" size={30} color="#DBFF00" style={{position: 'absolute'}}/>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="star" size={30} color="#DBFF00" style={{position: 'absolute'}}/>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="star" size={30} color="#DBFF00" style={{position: 'absolute'}}/>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                            </View>
                            <View style={styles.starTextContainer}>
                                <Text style={styles.starText}>
                                    4.0 and above
                                </Text>
                            </View>
                            { radioButton == 4 ? 
                            <View style={styles.radioButtonSelected}>
                                <View style={styles.radioButtonSelectedMiddle}/>
                            </View>
                            :
                            <TouchableOpacity onPress={() => setRadioButton(4)}>
                                <View style={styles.radioButton}/>
                            </TouchableOpacity>
                            }
                        </View>
                        <View style={styles.starLineContainer}>
                            <View style={styles.starContainer}>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="star" size={30} color="#DBFF00" style={{position: 'absolute'}}/>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="star" size={30} color="#DBFF00" style={{position: 'absolute'}}/>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="star" size={30} color="#DBFF00" style={{position: 'absolute'}}/>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                            </View>
                            <View style={styles.starTextContainer}>
                                <Text style={styles.starText}>
                                    3.0 and above
                                </Text>
                            </View>
                            { radioButton == 3 ? 
                            <View style={styles.radioButtonSelected}>
                                <View style={styles.radioButtonSelectedMiddle}/>
                            </View>
                            :
                            <TouchableOpacity onPress={() => setRadioButton(3)}>
                                <View style={styles.radioButton}/>
                            </TouchableOpacity>
                            }
                        </View>
                        <View style={styles.starLineContainer}>
                            <View style={styles.starContainer}>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="star" size={30} color="#DBFF00" style={{position: 'absolute'}}/>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="star" size={30} color="#DBFF00" style={{position: 'absolute'}}/>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                            </View>
                            <View style={styles.starTextContainer}>
                                <Text style={styles.starText}>
                                    2.0 and above
                                </Text>
                            </View>
                            { radioButton == 2 ? 
                            <View style={styles.radioButtonSelected}>
                                <View style={styles.radioButtonSelectedMiddle}/>
                            </View>
                            :
                            <TouchableOpacity onPress={() => setRadioButton(2)}>
                                <View style={styles.radioButton}/>
                            </TouchableOpacity>
                            }
                        </View>
                        <View style={styles.starLineContainer}>
                            <View style={styles.starContainer}>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="star" size={30} color="#DBFF00" style={{position: 'absolute'}}/>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                                <View style={[styles.starSection, {flex: 1, justifyContent: 'center', alignItems: 'center' }]}>
                                    <AntDesign name="staro" size={30} color="#000000" style={{position: 'absolute'}}/>
                                </View>
                            </View>
                            <View style={styles.starTextContainer}>
                                <Text style={styles.starText}>
                                    1.0 and above
                                </Text>
                            </View>
                            { radioButton == 1 ? 
                            <View style={styles.radioButtonSelected}>
                                <View style={styles.radioButtonSelectedMiddle}/>
                            </View>
                            :
                            <TouchableOpacity onPress={() => setRadioButton(1)}>
                                <View style={styles.radioButton}/>
                            </TouchableOpacity>
                            }
                        </View>
                    </View>
                    <View style={styles.containerBreak}/>
                        <View style={styles.textContainer}>
                            <Text style={[styles.ratingHeadingText, {paddingBottom: "4%"}]}>Attributes</Text>
                            <View style={styles.starLineContainer}>
                            { allowsDogs == true ? 
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setAllowsDogs(false)}>
                                <View style={styles.attributeBoxActive}>
                                    <Text style={styles.attributeText}>Allows Dogs</Text>
                                </View>
                            </TouchableOpacity>
                            :
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setAllowsDogs(true)}>
                                <View style={styles.attributeBox}>
                                    <Text style={styles.attributeText}>Allows Dogs</Text>
                                </View>
                            </TouchableOpacity>
                            }
                            { dineIn == true ? 
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setDineIn(false)}>
                                <View style={styles.attributeBoxActive}>
                                    <Text style={styles.attributeText}>Dine in</Text>
                                </View>
                            </TouchableOpacity>
                            :
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setDineIn(true)}>
                                <View style={styles.attributeBox}>
                                    <Text style={styles.attributeText}>Dine In</Text>
                                </View>
                            </TouchableOpacity>
                            }
                            </View>
                            <View style={styles.starLineContainer}>
                            { goodForGroups == true ? 
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setGoodForGroups(false)}>
                                <View style={styles.attributeBoxActive}>
                                    <Text style={styles.attributeText}>Good for Groups</Text>
                                </View>
                            </TouchableOpacity>
                            :
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setGoodForGroups(true)}>
                                <View style={styles.attributeBox}>
                                    <Text style={styles.attributeText}>Good for Groups</Text>
                                </View>
                            </TouchableOpacity>
                            }
                            { goodForChildren == true ? 
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setGoodForChildren(false)}>
                                <View style={styles.attributeBoxActive}>
                                    <Text style={styles.attributeText}>Good for Children</Text>
                                </View>
                            </TouchableOpacity>
                            :
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setGoodForChildren(true)}>
                                <View style={styles.attributeBox}>
                                    <Text style={styles.attributeText}>Good for Children</Text>
                                </View>
                            </TouchableOpacity>
                            }
                            </View>
                            <View style={styles.starLineContainer}>
                            { outdoorSeating == true ? 
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setOutdoorSeating(false)}>
                                <View style={styles.attributeBoxActive}>
                                    <Text style={styles.attributeText}>Outdoor Seating</Text>
                                </View>
                            </TouchableOpacity>
                            :
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setOutdoorSeating(true)}>
                                <View style={styles.attributeBox}>
                                    <Text style={styles.attributeText}>Outdoor Seating</Text>
                                </View>
                            </TouchableOpacity>
                            }
                            { delivery == true ? 
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setDelivery(false)}>
                                <View style={styles.attributeBoxActive}>
                                    <Text style={styles.attributeText}>Delivery</Text>
                                </View>
                            </TouchableOpacity>
                            :
                            <TouchableOpacity style={styles.attributeButtonWidth} onPress={() => setDelivery(true)}>
                                <View style={styles.attributeBox}>
                                    <Text style={styles.attributeText}>Delivery</Text>
                                </View>
                            </TouchableOpacity>
                            }
                            </View>
                        </View>
                        <View style={styles.containerBreak}/>
                            <CategoryFilter selectedCategories={selectedCategories} setSelectedCategories={setSelectedCategories} />
                        <View style={styles.containerBreak}/>

            </View>
            <View style={styles.deadSpace}/>
            <View style={styles.deaderSpace}/>
        </ScrollView>
        </KeyboardAvoidingView>
        <TouchableOpacity style={styles.resetButton} onPress={() => resetFilter()}>
            <Text style={styles.buttonText}>Reset</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.applyButton} onPress={() => saveFilter()}>
            <Text style={styles.buttonText}>Apply</Text>
        </TouchableOpacity>
    </Modal>
    );
}

const styles = StyleSheet.create({
    // Screen styling
    mainContainer: {
        backgroundColor: '#F5F7FC',
        height: '100%',
    },
    // Width of content
    widthContainer: {
        paddingLeft: '10%',
        paddingRight: '10%',
        backgroundColor: 'white',
    },
    // Container holding back arrow
    backContainer: {
        flexDirection: 'row',
        paddingLeft: '10%',
        width: '100%',
        backgroundColor: 'white',
    },
    // Information container
    informationContainer: {
        paddingTop: '4%',
        width: '100%',
        backgroundColor: 'white',
    },
    // Information heading text
    informationHeadingText: {
        fontWeight: '700',
        fontSize: 16,
        color: '#525357',
        paddingBottom: '4%',
        alignSelf: 'center',
    },
    // Text container
    textContainer: {
        paddingTop: '4%',
        paddingLeft: '10%',
        paddingRight: '10%',
        backgroundColor: 'white',
        paddingBottom: '4%',
    },
    // Rating heading container
    ratingHeadingText: {
        fontWeight: '700',
        fontSize: 16,
        color: '#525357',
    },
    // Keeping stars in a line container
    starLineContainer: {
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    // Star styling container
    starContainer: {
        paddingTop: '7%',
        width: '45%',
        backgroundColor: 'white',
        flexDirection: 'row',
        paddingBottom: '6%',
    },
    // Star text container
    starTextContainer: {
        flex: 1, 
        marginLeft: 15, 
    },
    // Text beside stars container
    starText: {
        position: 'absolute',
        bottom: '20%',
        left: -12,
        fontSize: 14,
        fontWeight: '600',
    },
    // custom radio button container
    radioButton: {
        marginTop: 8.6,
        borderRadius: 2000,
        borderWidth: 3,
        borderColor: '#525357',
        border: 1,
        height: 30,
        width: 30,
    },
    // custom radio button selected container
    radioButtonSelected: {
        marginTop: 8.6,
        borderRadius: 2000,
        borderWidth: 3,
        borderColor: '#1C58F2',
        border: 1,
        height: 30,
        width: 30,
        justifyContent: 'center',
        alignItems: 'center',
    },
    // custom radio button selected middle container
    radioButtonSelectedMiddle: {
        borderRadius: 2000,
        height: 18,
        width: 18,
        backgroundColor: '#1C58F2'
    },
    // reset button styling
    resetButton: {
        position: 'absolute',
        width: '40%',
        top: '88%',
        height: '6%',
        backgroundColor: '#BF360C',
        left: '8.5%',
        borderRadius: 20000,

        justifyContent: 'center',
        alignItems: 'center',
    },
    // apply button styling
    applyButton: {
        position: 'absolute',
        width: '40%',
        top: '88%',
        height: '6%',
        backgroundColor: '#1C58F2',
        right: '8.5%',
        borderRadius: 20000,

        justifyContent: 'center',
        alignItems: 'center',
    },
    // buttont text styling
    buttonText: {
        textAlign: 'center',
        fontSize: 20,
        fontWeight: '600',
        color: 'white'
    },
    // split between containers
    containerBreak: {
        width: '100%',
        height: 20,
        backgroundColor: '#F5F7FC',
    },
    // width for attribute button
    attributeButtonWidth: {
        width: "45%",
        marginBottom: "4%",
    },
    // attribute boxes
    attributeBox: {
        paddingTop: '17%',
        paddingBottom: '17%',
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 25,
        borderWidth: 3,
        borderColor: "#525357",
    },
    // styling when attribute button is active
    attributeBoxActive: {
        paddingTop: '17%',
        paddingBottom: '17%',
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 25,
        borderWidth: 3,
        borderColor: "#1C58F2",
        backgroundColor: 'rgba(28, 88, 242, 0.20)',
    },
    // styling of attribute text
    attributeText: {
        fontSize: 14,
        fontWeight: '600',
        color: 'black'
    },
    // Dead space so that while scrolling you see the correct colour
    deadSpace: {
        height: 500,
        backgroundColor: '#F5F7FC',
    },
    deaderSpace: {
        height: "40%",
        backgroundColor: '#F5F7FC',
    },
    // Text box for input
    textBox: {
        color: 'black',
        paddingHorizontal: 20,
        paddingVertical: 8,
        marginTop: 12,
        borderRadius: 18,
        fontSize: 16,
        fontWeight: '500',
        borderWidth: 3,
        borderColor: "#525357",
    },
});

export default FilterScreen