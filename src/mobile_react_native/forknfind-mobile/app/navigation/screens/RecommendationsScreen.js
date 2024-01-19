import React, { useState} from 'react';
// import { View, Text, StyleSheet,  } from 'react-native';
import { View, Text, Switch, TouchableOpacity, Modal, TouchableHighlight, TextInput, StyleSheet} from 'react-native';

import { EvilIcons } from '@expo/vector-icons';
import { ScrollView } from 'react-native-gesture-handler';

export default function RecommendationsScreen({ navigation }) {

    const [detailsModalVisibility, setDetailsModalVisibility] = useState(false);

    const toggleModal = (option) => {
    //setOption(option);
        if (option === 'item1') { // Modal for account details
            setDetailsModalVisibility(!detailsModalVisibility);
        }
    }
    return (
        <ScrollView style={styles.container}>
            <Text style={styles.titleStyle}>Recommendations</Text>
            
            {/* Item 1 */}
            <TouchableOpacity style={styles.itemContainer} onPress={() => toggleModal('item1')}>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>Apache Pizza</Text>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>€€</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                        <EvilIcons style={{padding: 5,}}name="star" size={24} color="black" />
                        <Text style={{padding: 5,}}>4/5</Text>
                    </View>
                    <Text style={{padding: 5, }}>8.5km</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Pizza</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Italian</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '35%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Fast Food</Text>
                    </View>
                </View>
            </TouchableOpacity>

            <TouchableOpacity style={styles.itemContainer} onPress={() => toggleModal('item1')}>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>Apache Pizza</Text>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>€€</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                        <EvilIcons style={{padding: 5,}}name="star" size={24} color="black" />
                        <Text style={{padding: 5,}}>4/5</Text>
                    </View>
                    <Text style={{padding: 5, }}>8.5km</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Pizza</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Italian</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '35%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Fast Food</Text>
                    </View>
                </View>
            </TouchableOpacity>

            <TouchableOpacity style={styles.itemContainer} onPress={() => toggleModal('item1')}>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>Apache Pizza</Text>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>€€</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                        <EvilIcons style={{padding: 5,}}name="star" size={24} color="black" />
                        <Text style={{padding: 5,}}>4/5</Text>
                    </View>
                    <Text style={{padding: 5, }}>8.5km</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Pizza</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Italian</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '35%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Fast Food</Text>
                    </View>
                </View>
            </TouchableOpacity>

            <TouchableOpacity style={styles.itemContainer} onPress={() => toggleModal('item1')}>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>Apache Pizza</Text>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>€€</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                        <EvilIcons style={{padding: 5,}}name="star" size={24} color="black" />
                        <Text style={{padding: 5,}}>4/5</Text>
                    </View>
                    <Text style={{padding: 5, }}>8.5km</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Pizza</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Italian</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '35%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Fast Food</Text>
                    </View>
                </View>
            </TouchableOpacity>

            <TouchableOpacity style={styles.itemContainer} onPress={() => toggleModal('item1')}>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>Apache Pizza</Text>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>€€</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                        <EvilIcons style={{padding: 5,}}name="star" size={24} color="black" />
                        <Text style={{padding: 5,}}>4/5</Text>
                    </View>
                    <Text style={{padding: 5, }}>8.5km</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Pizza</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Italian</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '35%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Fast Food</Text>
                    </View>
                </View>
            </TouchableOpacity>

            <TouchableOpacity style={styles.itemContainer} onPress={() => toggleModal('item1')}>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>Apache Pizza</Text>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>€€</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                        <EvilIcons style={{padding: 5,}}name="star" size={24} color="black" />
                        <Text style={{padding: 5,}}>4/5</Text>
                    </View>
                    <Text style={{padding: 5, }}>8.5km</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Pizza</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Italian</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '35%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Fast Food</Text>
                    </View>
                </View>
            </TouchableOpacity>

            <TouchableOpacity style={styles.itemContainer} onPress={() => toggleModal('item1')}>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>Apache Pizza</Text>
                    <Text style={{ padding: 5, fontWeight: 'bold'}}>€€</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'space-between'}}>
                    <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                        <EvilIcons style={{padding: 5,}}name="star" size={24} color="black" />
                        <Text style={{padding: 5,}}>4/5</Text>
                    </View>
                    <Text style={{padding: 5, }}>8.5km</Text>
                </View>
                <View style={{flexDirection: 'row', justifyContent: 'flex-start'}}>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Pizza</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '25%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Italian</Text>
                    </View>
                    <View style={{borderWidth: 1, padding: 10, borderColor: '#ccc', borderRadius: 10, justifyContent: 'space-evenly', flexDirection: 'row', width: '35%', backgroundColor: '#ccc', margin: 5}}>
                        <Text>Fast Food</Text>
                    </View>
                </View>
            </TouchableOpacity>

            {/* Item 1 modal */}
            <Modal animationType="slide" transparent={true} visible={detailsModalVisibility} onRequestClose={() => toggleModal('item1')}>
                <ScrollView contentContainerStyle={styles.modalContentContainer} showsVerticalScrollIndicator={false}>
                    <View style={styles.modalContent}>
                        <View>
                            <TouchableOpacity style={styles.backButton} onPress={() => toggleModal('item1')}>
                                <EvilIcons name="arrow-left" size={24} color="black" />
                            </TouchableOpacity>
                            <Text style={styles.modalTitle}>Reviews</Text>
                        </View>

                        <View style={styles.modalDetailsBlock}>
                            <Text style={{color: 'grey'}}>Review from: </Text>
                            <Text style={{fontWeight: 'bold'}}>Joe Something</Text>
                        </View>
                        <View style={{borderWidth: 1, borderColor: 'green', borderRadius: 10, padding: 10}}>
                            <Text>This place was really good, will order food here again!</Text>
                        </View>

                        <View style={styles.modalDetailsBlock}>
                            <Text style={{color: 'grey'}}>Review from: </Text>
                            <Text style={{fontWeight: 'bold'}}>Joe Other</Text>
                        </View>
                        <View style={{borderWidth: 1, borderColor: 'red', borderRadius: 10, padding: 10}}>
                            <Text>This place was terrible good, will never order food here again!</Text>
                        </View>

                    </View>
                </ScrollView>
            </Modal>
        </ScrollView>

        
    );
};

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
    itemContainer: {
        // flexDirection: 'row',
        // justifyContent: 'space-between',
        // alignItems: 'center',
        width: '80%',
        alignSelf: 'center',
        marginBottom: 20,
        borderWidth: 1,
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
        marginTop: 50,
        ...StyleSheet.absoluteFillObject,
        backgroundColor: 'white',
        padding: 20,
        borderRadius: 10,
        width: '100%',
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
    modalDetailsBlock: {
        marginTop: 30,
        marginBottom: 10,
        flexDirection: 'row',
        justifyContent: 'flex-start'
    },
    modalContentContainer: {
        flexGrow: 1,
      },
});