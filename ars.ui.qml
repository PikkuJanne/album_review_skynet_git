import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12

Window {
    visible: true
    width: 1024
    height: 768

    Rectangle {
        anchors.fill: parent

        Image {
            source: "terminator.png"
            anchors.fill: parent
            fillMode: Image.PreserveAspectCrop
        }

        Text {
            width: 822
            height: 124
            color: "#fefefe"
            text: qsTr("Album Review Skynet")
            font.bold: true
            font.pointSize: 60
            anchors.verticalCenterOffset: -245
            anchors.horizontalCenterOffset: 0
            anchors.centerIn: parent
        }

        TextField {
            id: textField
            x: 169
            y: 254
            text: albumReviewHandler.band_name
            placeholderText: qsTr("Band name")
        }

        RadioButton {
            id: radioButton
            x: 432
            y: 254
            checked: albumReviewHandler.is_rock_album
            font.bold: true
            font.pointSize: 15
    
            Label {
                text: qsTr("Rock Album")
                color: "#ffffff"
                y: radioButton.y - 275 
                
           }
        }       

        RadioButton {
            id: radioButton1
            x: 432
            y: 328
            font.bold: true
            font.pointSize: 15
    
            Label {
                text: qsTr("Pop Album")
                color: "#ffffff"
                y: radioButton1.y - 350 
                
            }
        }

        TextField {
            id: textField1
            x: 169
            y: 328
            text: albumReviewHandler.album_name
            placeholderText: qsTr("Album name")
        }

        Text {
            id: text1
            x: 35
            y: 262
            width: 118
            height: 25
            color: "#ffffff"
            text: qsTr("Band Name:")
            font.pixelSize: 20
        }

        Text {
            id: text2
            x: 35
            y: 335
            width: 118
            height: 26
            color: "#fbfbfb"
            text: qsTr("Album Name:")
            font.pixelSize: 20
        }

        Text {
            id: text4
            x: 621
            y: 254
            width: 111
            height: 26
            color: "#ffffff"
            text: qsTr("Lead Songs(hit Enter after each song):")
            font.pixelSize: 20
        }

        Item {
            id: textEditContainer
            x: 621
            y: 293
            width: 365
            height: 159

            Rectangle {
                anchors.fill: parent
                color: "white" 

                TextEdit {
                    id: textEdit
                    anchors.fill: parent
                    text: qsTr("")
                    font.pixelSize: 18
                    selectedTextColor: "#010101"
                    selectionColor: "#f8f8fc"
                    color: "#000000" 
                }
            }
        }

        Button {
            id: generateButton
            objectName: "generateButton"
            x: 169 // Align with other text fields
            y: textField1.y + textField1.height + 50 
            text: qsTr("Generate Review")
            onClicked: albumReviewHandler.generate_review(textEdit.text) 
            textEdit.text = ""; 
        }

        Text {
            id: textAlbumReview
            x: 28 // Same x position as the reviewContainer
            y: 510 // A bit above the reviewContainer
            color: "#ffffff"
            text: qsTr("Album Review")
            font.pixelSize: 20
        }

        Item {
            id: reviewContainer
            x: 28
            y: 550
            width: 958
            height: 174

            Rectangle {
                anchors.fill: parent
                color: "white" 

                TextArea {
                    id: reviewTextArea
                    anchors.fill: parent
                    text: albumReviewHandler.review
                    placeholderText: qsTr("Album Review")
                    color: "#000000" 
                    readOnly: true 
                    wrapMode: TextArea.Wrap 
                }
            }
        }
    }
}
