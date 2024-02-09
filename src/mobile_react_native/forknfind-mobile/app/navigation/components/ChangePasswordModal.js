import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, Modal, TouchableOpacity, StatusBar, TextInput, KeyboardAvoidingView } from 'react-native';
import ChangePasswordAPIRequest from '../requests/ChangePasswordAPIRequest';

// Functional Component ChangePasswordModal
// visible - use state identifying whether the modal is visible or not
// onClose - the trigger for closing the modal view
const ChangePasswordModal = ({ visible, onClose}) => {

    const [currentPassword, setCurrentPassword] = useState("");
    const [password, setPassword] = useState("");
    const [passwordCheck, setPasswordCheck] = useState("");
    const [responseData, setResponseData] = useState("")

    const resetFilter = () => {

        setCurrentPassword("");
        setPassword("");
        setPasswordCheck("");
        setResponseData("");
        onClose();
    }

    // On save filter save to use state and leave modal
    const saveFilter = () => {

        if (password == passwordCheck) {
            // Pass to API request
            console.log(currentPassword, password)
            ChangePasswordAPIRequest(currentPassword, password, setResponseData)
        }
        else {
            console.log("passwords not the same i think")
        }
    }

    const currentPasswordUpdate = (text) => {

        setCurrentPassword(text);
    }

    // Logic for updating password use state
    const passwordUpdate = (text) => {

        setPassword(text);
    }

    // Logic for updating passwordCheck use state
    const passwordCheckUpdate = (text) => {

        setPasswordCheck(text);
    }

    useEffect(() => {
        
        if (responseData["detail"] == "Success") {
            resetFilter()
        }
    }, [responseData]);

    return (
        <Modal
        animationType="slide"
        transparent={true}
        visible={visible}
        onRequestClose={onClose}
    >
        <StatusBar barStyle="light-content" />
        <KeyboardAvoidingView
        style={{ flex: 1 }}
        behavior="padding" 
        enabled
    >
        <View style={{ flex: 1, backgroundColor: 'rgba(0, 0, 0, 0.7)' }}>
            <View style={[styles.modalContainer, {paddingBottom: 25}]}>
                <View style={styles.modalPadding}>
                <Text style={[styles.textBoxHeading, { marginTop: 15 }]}>
                        Current Password
                    </Text>
                    <TextInput
                        placeholder="current password"
                        placeholderTextColor="#797979"
                        autoCapitalize='none'
                        style={styles.textBox}
                        autoCorrect={false}
                        value={currentPassword}
                        onChangeText={currentPasswordUpdate}
                        secureTextEntry={true}
                    />
                    <Text style={[styles.textBoxHeading, { marginTop: 15 }]}>
                        New Password
                    </Text>
                    <TextInput
                        placeholder="new password"
                        placeholderTextColor="#797979"
                        autoCapitalize='none'
                        style={styles.textBox}
                        autoCorrect={false}
                        value={password}
                        onChangeText={passwordUpdate}
                        secureTextEntry={true}
                    />
                    <Text style={[styles.textBoxHeading, { marginTop: 15 }]}>
                        Retype New Password
                    </Text>
                    <TextInput
                        placeholder="retype new password"
                        placeholderTextColor="#797979"
                        autoCapitalize='none'
                        style={styles.textBox}
                        autoCorrect={false}
                        value={passwordCheck}
                        onChangeText={passwordCheckUpdate}
                        secureTextEntry={true}
                    />
                </View>
            </View>
        </View>
        {/* Buttons for applying or back from modal */}
        <TouchableOpacity style={styles.resetButton} onPress={() => resetFilter()}>
            <Text style={styles.buttonText}>Back</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.applyButton} onPress={() => saveFilter()}>
            <Text style={styles.buttonText}>Apply</Text>
        </TouchableOpacity>
    </KeyboardAvoidingView>
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
    // Reset button styling
    resetButton: {
        position: 'absolute',
        width: '40%',
        top: '88%',
        height: 57,
        backgroundColor: '#BF360C',
        left: '8.5%',
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
    },
    // Headings for the titles above the text inputs
    textBoxHeading: {
        fontWeight: '700',
        fontSize: 16,
        color: '#525357',
        paddingBottom: '1%',
    },
    // Text box css
    textBox: {
        color: 'black',
        paddingHorizontal: 20,
        paddingVertical: 8,
        borderRadius: 10,
        fontSize: 16,
        fontWeight: '500',
        borderWidth: 2,
        borderColor: "#525357",
    },
});

export default ChangePasswordModal;