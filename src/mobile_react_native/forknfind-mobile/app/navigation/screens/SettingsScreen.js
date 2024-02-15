import React, { useState} from 'react';
// import { View, Text, StyleSheet,  } from 'react-native';
import { View, Text, StyleSheet, SafeAreaView, StatusBar} from 'react-native';
import { AntDesign } from '@expo/vector-icons';
import { TouchableOpacity } from 'react-native-gesture-handler';
import ChangePasswordModal from '../components/ChangePasswordModal';
import AccountInformationModal from '../components/AccountinformationModal';

export default function SettingsScreen({ navigation, setIsLoggedIn }) {

    const [modalPasswordChangeVisible, setModalPasswordChangeVisible] = useState(false);
    const [modalAccountInformation, setModalAccountInformation] = useState(false)

    const logoutAccount = () => {

        username_global = ""
        access_global = ""
        setIsLoggedIn(false)
    }

    return (
        <View style={{backgroundColor: '#F5F7FC'}}>
            <SafeAreaView style={styles.container}/>
            <StatusBar barStyle="dark-content" />
            <View style={styles.settingsBox}>
                <TouchableOpacity style={styles.settingsLine}onPress={() => {setModalAccountInformation(true)}}>
                    <Text style={styles.settingTitle}>
                        Account Details
                    </Text>
                    <View style={styles.settingIcon}>
                        <AntDesign name="arrowright" size={24} color="black" />
                    </View>
                </TouchableOpacity>
                <TouchableOpacity style={styles.settingsLine} onPress={() => {setModalPasswordChangeVisible(true)}}>
                    <Text style={styles.settingTitle}>
                        Change Password
                    </Text>
                    <View style={styles.settingIcon}>
                        <AntDesign name="arrowright" size={24} color="black" />
                    </View>
                </TouchableOpacity>
                <TouchableOpacity style={styles.settingsLine} onPress={() => {logoutAccount()}}>
                    <Text style={styles.settingTitle}>
                        Logout
                    </Text>
                    <View style={styles.settingIcon}>
                        <AntDesign name="arrowright" size={24} color="black" />
                    </View>
                </TouchableOpacity>
            </View>
            <ChangePasswordModal visible={modalPasswordChangeVisible} onClose={() => setModalPasswordChangeVisible(false)} />
            <AccountInformationModal visible={modalAccountInformation} onClose={() => setModalAccountInformation(false)} />
            <View style={{height: 900, backgroundColor: "#F5F7FC"}} />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#F5F7FC'
    },
    settingsBox: {
        marginTop: '10%',
        width: '100%',
        paddingHorizontal: '15%',
    },
    settingsLine: {
        borderBottomWidth: 2,
        borderColor: '#ccc',
        borderBottomRadius: 10,
        flexDirection: 'row', 
        justifyContent: 'space-between',
    },
    settingTitle: {
        paddingLeft: '5%',
        paddingTop: 25,
        paddingBottom: 5,
        fontSize: 18,
        color: '#333333'
    },
    settingIcon: {
        top: 24,
        paddingRight: '5%', 
    }
});