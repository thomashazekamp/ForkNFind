import React, { useState } from 'react';
import { View, Text, StyleSheet, Modal, TouchableOpacity, StatusBar } from 'react-native';

// Functional Component MapFilter
// visible - use state identifying whether the modal is visible or not
// onClose - the trigger for closing the modal view
// setSortVisual - for displaying the sort type
const MapFilter = ({ visible, onClose, setSortVisual}) => {

    // Use states
    const [radioButton, setRadioButton] = useState(1);

    // On save filter save to use state and leave modal
    const saveFilter = () => {

        if (radioButton == 1) {
            setSortVisual("All")
        }
        if (radioButton == 2) {
            setSortVisual("Open")
        } 
        if (radioButton == 3) {
            setSortVisual("Closed")
        } 
        if (radioButton == 4) {
            setSortVisual("Recommended")
        } 
        onClose();
    }

    return (
        <Modal
        animationType="slide"
        transparent={true}
        visible={visible}
        onRequestClose={onClose}
    >
        <StatusBar barStyle="light-content" />
        <View style={{flex: 1, backgroundColor: 'rgba(0, 0, 0, 0.7)'}}>
            <View style={styles.modalContainer}>
                <View style={styles.modalPadding} >
                    <View style={styles.option}>
                        {/* Use custom radio button design that can be selected, on click update the selected choice of sorting */}
                        <Text style={styles.textOption}>All</Text>
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
                    <View style={styles.option}>
                        <Text style={styles.textOption}>Open</Text>
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
                    <View style={styles.option}>
                        <Text style={styles.textOption}>Closed</Text>
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
                    <View style={styles.option}>
                        <Text style={styles.textOption}>Recommended</Text>
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
                </View>
            </View>
        </View>
        {/* Buttons for applying or back from modal */}
        <TouchableOpacity style={styles.applyButton} onPress={() => saveFilter()}>
            <Text style={styles.buttonText}>Apply</Text>
        </TouchableOpacity>
    </Modal>
    );
}

const styles = StyleSheet.create({
    // styling to fit to content
    modalContainer: {
        backgroundColor: "white",
        position: 'absolute',
        bottom: 0,
        width: "100%",
        borderTopLeftRadius: 30,
        borderTopRightRadius: 30,
    },
    // Bottom padding where buttons are
    modalPadding: {
        paddingTop: 20,
        paddingLeft: "7.5%",
        paddingRight: "7.5%",
        paddingBottom: 140,
    },
    // Radio button design
    radioButton: {
        marginTop: 8.6,
        borderRadius: 2000,
        borderWidth: 3,
        borderColor: '#525357',
        border: 1,
        height: 30,
        width: 30,
    },
    // Selected radio button design
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
    // Middle of radio button when selected
    radioButtonSelectedMiddle: {
        borderRadius: 2000,
        height: 18,
        width: 18,
        backgroundColor: '#1C58F2'
    },
    // Apply button styling
    applyButton: {
        position: 'absolute',
        width: '50%',
        top: '88%',
        height: '6%',
        backgroundColor: '#1C58F2',
        left: '25%',
        borderRadius: 20000,

        justifyContent: 'center',
        alignItems: 'center',
    },
    // Button text styling
    buttonText: {
        textAlign: 'center',
        fontSize: 20,
        fontWeight: '600',
        color: 'white'
    },
    // Splliting radio button and text
    option: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        paddingBottom: '2%',
    },
    // Text styling
    textOption: {
        paddingTop: '3.5%',
        fontSize: 16,
        fontWeight: '600',
    }
});

export default MapFilter