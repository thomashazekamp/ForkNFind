import React, { useState} from 'react';
// import { View, Text, StyleSheet,  } from 'react-native';
import { View, Text, Switch, TouchableOpacity, Modal, TouchableHighlight, TextInput, StyleSheet} from 'react-native';

import { Entypo } from '@expo/vector-icons';
import { EvilIcons } from '@expo/vector-icons';

export default function SettingsScreen({ navigation }) {
    const [passwordModalVisibility, setPasswordModalVisibility] = useState(false);
    const [detailsModalVisibility, setDetailsModalVisibility] = useState(false);
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const toggleModal = (option) => {
    //setOption(option);
        if (option === 'details') { // Modal for account details
            setDetailsModalVisibility(!detailsModalVisibility);
        }
        else if (option === 'password') { // Modal for change password
            setPasswordModalVisibility(!passwordModalVisibility);
        }
        else if (option === 'save') { // Close modal after saving
            setPasswordModalVisibility(false);
            setDetailsModalVisibility(false);
        }
    };

    const savePassword = () => { // Provide alert & close tab
        alert('New password saved!');
        toggleModal('save'); // Close the modal after saving
    };

    return (
        <View style={styles.container}>
            <Text style={styles.titleStyle}>Settings</Text>

            <TouchableOpacity style={styles.settingOption} onPress={() => toggleModal('details')}>
                <Text>Account Details</Text>
                {/* <Entypo name="arrow-long-right" size={24} color="black" /> */}
                <EvilIcons name="arrow-right" size={24} color="black" />
            </TouchableOpacity>

            <TouchableOpacity style={styles.settingOption} onPress={() => toggleModal('password')}>
                <Text>Change Password</Text>
                <EvilIcons name="arrow-right" size={24} color="black" />
            </TouchableOpacity>

            {/* Account details modal */}
            <Modal animationType="slide" transparent={true} visible={detailsModalVisibility} onRequestClose={() => toggleModal('details')}>
                <View style={styles.modalContainer}>
                    <View style={styles.modalContent}>
                        <TouchableOpacity style={styles.backButton} onPress={() => toggleModal('details')}>
                            <EvilIcons name="arrow-left" size={24} color="black" />
                        </TouchableOpacity>
                        <Text style={styles.modalTitle}>Account Details</Text>
                        <Text>Name: Test</Text>
                        <Text>Email: Test@gmail.com</Text>
                        <Text>Location: Dublin, Ireland</Text>
                        <Text>Num. of Reviews: 5</Text>
                    </View>
                </View>
            </Modal>

            {/* Change password modal */}
            <Modal animationType="slide" transparent={true} visible={passwordModalVisibility} onRequestClose={() => toggleModal('password')}>
                <View style={styles.modalContainer}>
                    <View style={styles.modalContent}>
                        <TouchableOpacity style={styles.backButton} onPress={() => toggleModal('password')}>
                            <EvilIcons name="arrow-left" size={24} color="black" />
                        </TouchableOpacity>
                        <Text style={styles.modalTitle}>Change Password</Text>
                        <Text style={styles.modalText}>Choose a new password</Text>

                        <View>
                            <TextInput placeholder="New Password" secureTextEntry style={styles.modalInputBox} value={password} onChangeText={(text) => setPassword(text)}/>
                        </View>

                        <View>
                            <TextInput placeholder="Confirm Password" secureTextEntry style={styles.modalInputBox} value={confirmPassword} onChangeText={(text) => setConfirmPassword(text)}/>
                        </View>

                        <View style={styles.modalButtonContainer}>
                            <TouchableOpacity style={styles.modalButton} onPress={savePassword}>
                                <Text style={styles.modalButtonText}>Save Password</Text>
                            </TouchableOpacity>
                        </View>
                    </View>
                </View>
            </Modal>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
    },
    titleStyle: {
        fontSize: 30,
        fontWeight: 'bold',
        marginBottom: 20,
        alignSelf: 'center',
    },
    settingOption: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        width: '80%',
        alignSelf: 'center',
        marginBottom: 20,
        borderBottomWidth: 1,
        borderColor: '#ccc',
        padding: 10,
        borderRadius: 10,
    },
    modalContainer: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
    },
    modalContent: {
        backgroundColor: 'white',
        padding: 20,
        borderRadius: 10,
        width: '80%',
    },
    modalTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 10,
        alignSelf: 'center',
    },
    modalText: {
        marginBottom: 10,
        alignSelf: 'center',
        color: 'grey'
    },
    modalInputBox: {
        marginBottom: 10,
        borderBottomWidth: 1,
        borderColor: '#ccc',
        padding: 8,
        borderRadius: 5,
    },
    modalButtonContainer: {
        flexDirection: 'row',
        marginTop: 10,
    },
    modalButton: {
        borderWidth: 1,
        borderColor: '#ccc',
        padding: 10,
        borderRadius: 10,
        flex: 1,
        marginRight: 5,
    },
    modalButtonText: {
        color: 'black',
        textAlign: 'center',
    },
    backButton: {
        alignSelf: 'flex-start',
    },
});