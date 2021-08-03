import 'package:flutter/material.dart';
import 'availablePrograms.dart';
import 'list_of_programs_widget.dart';

class chooseProgram extends StatefulWidget {
  const chooseProgram({Key? key}) : super(key: key);

  @override
  _chooseProgramState createState() => _chooseProgramState();
}

class _chooseProgramState extends State<chooseProgram> {

  var _foundPrograms = [];
  //@override
  initState() {
    // at the beginning, all users are shown
    _foundPrograms = list_of_Programs;
    super.initState();
  }

  // This function is called whenever the text field changes
  void _runFilter(String enteredKeyword) {
    var response = [];
    if (enteredKeyword.isEmpty) {
      // if the search field is empty or only contains white-space, we'll display all users
      response = list_of_Programs;
    } else {
      // we use the toLowerCase() method to make it case-insensitive
      response = list_of_Programs.where((program)=>
      program.toString().toLowerCase().contains(enteredKeyword.toLowerCase())).toList();
    }

    // Refresh the UI
    setState(() {
      _foundPrograms = response;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: Column(
          children: [
            SizedBox(
              height: 20,
            ),
            TextField(
              onChanged: (value) => _runFilter(value),
              decoration: InputDecoration(
                  labelText: 'Search', suffixIcon: Icon(Icons.search,
              color: Color.fromRGBO(200, 100, 255, 0.25),),
              ),
            ),
            SizedBox(
              height: 20,
            ),
            Expanded(
              child: _foundPrograms.length > 0
                  ? ListView.builder(
                itemCount: _foundPrograms.length,
                itemBuilder: (context, index) => Card(
                  key: ValueKey(index),
                  color: Color.fromRGBO(200, 100, 255, 0.25),
                  elevation: 4,
                  margin: EdgeInsets.symmetric(vertical: 10),
                  child: ListTile(
                    onTap: (){
                      print('${_foundPrograms[index]} was tapped');
                    },
                    leading: Image.asset(
                      'images/tired.jpg'
                    ),
                    title: Text(_foundPrograms[index]),
                    subtitle: Text(
                        '${lorem}'),
                  ),
                ),
              )
                  : Text(
                'No results found',
                style: TextStyle(fontSize: 24),
              ),
            ),
          ],
        ),
      ),
    );
  }
}


var lorem = '''
Ln reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur''';

Container programList(
    context, gridOrFalse, programName, programInfo, programPic, department) {
  return Container(
    width: MediaQuery.of(context).size.width * 0.2,
    child: Card(
        child: ListTile(
      leading: CircleAvatar(
        child: Image(
          image: NetworkImage(programPic),
        ),
      ),
      title: Text(programName),
      subtitle: Text(programInfo),
      trailing: department,
    )),
  );
}
