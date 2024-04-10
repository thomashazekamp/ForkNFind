import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Modal, TouchableOpacity, StatusBar, TextInput, KeyboardAvoidingView } from 'react-native';
import GetUserInformationAPIRequest from '../requests/GetUserInformationAPIRequest';

// Functional Component ChangePasswordModal
// visible - use state identifying whether the modal is visible or not
// onClose - the trigger for closing the modal view
const AccountInformationModal = ({ visible, onClose}) => {

    const [data, setData] = useState("")

    useEffect(() => {
        
        GetUserInformationAPIRequest(setData)

    }, []);

    return (
        <Modal
        animationType="slide"
        transparent={true}
        visible={visible}
        onRequestClose={onClose}
    >
        <StatusBar barStyle="light-content" />
        <View style={{ flex: 1, backgroundColor: 'rgba(0, 0, 0, 0.7)' }}>
            <View style={[styles.modalContainer, {paddingBottom: 25}]}>
                <View style={styles.modalPadding}>
                    <View style={styles.informationContainer}>
                        <View style={styles.leftInformationContainer}>
                            <Text style={styles.informationHeadingText}>First Name</Text>
                            <Text style={[styles.informationContentText, {paddingLeft: '5%'}]}>{data.first_name}</Text>
                        </View>
                        <View style={styles.rightInformationContainer}>
                            <Text style={styles.informationHeadingText}>Last Name</Text>
                            <Text style={[styles.informationContentText, {paddingLeft: '5%'}]}>{data.last_name}</Text>
                        </View>
                    </View>
                    <View style={styles.informationContainer}>
                        <View style={{paddingLeft: "5%",}}>
                            <Text style={styles.informationHeadingText}>Username</Text>
                            <Text style={[styles.informationContentText, {paddingLeft: '2.5%'}]}>{data.username}</Text>
                        </View>
                    </View>
                    <View style={styles.informationContainer}>
                        <View style={{paddingLeft: "5%",}}>
                            <Text style={styles.informationHeadingText}>Email</Text>
                            <Text style={[styles.informationContentText, {paddingLeft: '2.5%'}]}>{data.email}</Text>
                        </View>
                    </View>
                </View>
            </View>
        </View>
        {/* Buttons for applying or back from modal */}
        <TouchableOpacity style={styles.resetButton} onPress={() => onClose()}>
            <Text style={styles.buttonText}>Close</Text>
        </TouchableOpacity>
    </Modal>
    );
}

const styles = StyleSheet.create({
    // styling to fit content
    modalContainer: {
        backgroundColor: "white",
        position: 'absolute',
        bottom: 0,
        width: "100%",
        borderTopLeftRadius: 30,
        borderTopRightRadius: 30,
    },
    // Bottom padding where the buttons are
    modalPadding: {
        paddingTop: 20,
        paddingLeft: "7.5%",
        paddingRight: "7.5%",
        paddingBottom: 140,
    },
    // Radio button design
    // Reset button styling
    resetButton: {
        position: 'absolute',
        width: '50%',
        top: '88%',
        height: 57,
        backgroundColor: '#1C58F2',
        left: '25%',
        borderRadius: 20000,

        justifyContent: 'center',
        alignItems: 'center',
    },
    // Apply button styling
    applyButton: {
        position: 'absolute',
        width: '40%',
        top: '88%',
        height: 57,
        backgroundColor: '#1C58F2',
        right: '8.5%',
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
        paddingLeft: "5%",
    },
    // information on right
    rightInformationContainer: {
        width: "50%",
        paddingLeft: '5%',
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
});

export default AccountInformationModal;