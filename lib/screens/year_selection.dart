import 'package:flutter/material.dart';
import 'availablePrograms.dart';

class yearSelection extends StatefulWidget {
  

  @override
  _yearSelectionState createState() => _yearSelectionState();
}

class _yearSelectionState extends State<yearSelection> {

  String name_of_program = 'computer';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: OrientationBuilder(
          builder: (context, orientation)=>
          orientation==Orientation.portrait?portrait_grid(name_of_program):landscape_listTiles(name_of_program),
        ),
      )
    );
  }
}

class portrait_grid extends StatelessWidget {
  String name_of_program;

  portrait_grid(this.name_of_program);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [

        SizedBox(
            height: MediaQuery.of(context).size.height*0.15
        ),
        Expanded(
            child: GridView.builder(
                itemCount: programYearCourses['${this.name_of_program}']['years'],
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2,
                    crossAxisSpacing: 5.0,
                    mainAxisSpacing: 10.0
                ),
                itemBuilder: (BuildContext context, int index){
                  return Card(
                    shadowColor: Color.fromRGBO(255, 100, 255, 1.0),
                    child: Container(
                      decoration: BoxDecoration(
                          color: Color.fromRGBO(200, 100, 255, 0.25)
                      ),
                      child: ListTile(
                        onTap: (){
                          print('portrait year ${index + 1} pressed');
                        },
                        title: Text('Year ${index + 1}'),
                      ),
                    ),
                  );
                })
        )
      ],
    );
  }
}

class landscape_listTiles extends StatelessWidget {
  //String name_of_program = 'computer';
  String name_of_program;

  landscape_listTiles(this.name_of_program);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Expanded(
          child: ListView.builder(
              itemCount: programYearCourses['${this.name_of_program}']['years'],
              itemBuilder: (BuildContext context, int index){
                return Card(
                  margin: EdgeInsets.all(12.0),
                  shadowColor: Color.fromRGBO(255, 100, 255, 1.0),
                  child: Container(
                    decoration: BoxDecoration(
                        color: Color.fromRGBO(200, 100, 255, 0.25)
                    ),
                    child: ListTile(
                      onTap: (){
                        print('landScape year ${index +1} pressed');
                      },
                      title: Text('Year ${index + 1}'),
                    ),
                  ),
                );
              }),
        )
      ],
    );
  }
}





