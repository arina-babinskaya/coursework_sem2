class MixedResponsibilities {
private:
    int userId;
    int userAge;
    int fileSize;
    int connectionStatus;

public:
    int getUserAge() {
        return userAge;
    }

    void setUserAge(int value) {
        userAge = value;
    }

    int getFileSize() {
        return fileSize;
    }

    void setFileSize(int value) {
        fileSize = value;
    }

    int getConnectionStatus() {
        return connectionStatus;
    }

    void setConnectionStatus(int value) {
        connectionStatus = value;
    }

    int getUserId() {
        return userId;
    }
};
