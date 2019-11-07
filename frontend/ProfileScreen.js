class ProfileScreen extends React.Component {
    static navigationOptions = {
      title: 'Welcome',
    };
    render() {
      const {navigate} = this.props.navigation;
      return (
        <Button
          title="Go to Home Screen"
          onPress={() => navigate('Profile', {name: 'Jane'})}
        />
      );
    }
  }