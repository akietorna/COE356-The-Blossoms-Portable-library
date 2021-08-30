import 'package:flutter/material.dart';
import 'availablePrograms.dart';

class Courses extends StatefulWidget {
  List list_of_courses;

  Courses (this.list_of_courses);

  @override
  State<Courses> createState() => _CoursesState();
}



class _CoursesState extends State<Courses> with TickerProviderStateMixin{

  TabController _controller;
  int _initialTabIndex = 0;
  var _foundPrograms = [];

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _foundPrograms = list_of_Programs;
    _controller = TabController(length: 2, vsync: this);

    _controller.addListener(() {
      setState(() {
        print(_controller.index);
        _initialTabIndex = _controller.index;
      });
    });
  }

  @override
  void dispose() {
    // TODO: implement dispose
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        body: NestedScrollView(
            headerSliverBuilder:
                (BuildContext context, bool innerBoxIsScrolled) {
              return <Widget>[
                SliverAppBar(
                  actions: [
                    //TODO: Quick search for course
                  ],
                  title: Text('program and year goes here'),
                  expandedHeight: 160.0,
                  pinned: true,
                  floating: true,
                  bottom: TabBar(
                    controller: _controller,
                    onTap: (_) {
                      print('tapped ${_} page');
                    },
                    tabs: [
                      Tab(
                        child: Text('First Semester'),
                      ),
                      Tab(
                        child: Text('Second Semester'),
                      )
                    ],
                  ),
                )
              ];
            },
            body: TabBarView(
              controller: _controller,
              children: [

                ListView.builder(
                    itemCount: widget.list_of_courses[0].length,
                    itemBuilder: (BuildContext context, int index){
                      return Card(
                        child: Container(
                          child: ListTile(
                            onTap: (){
                              print('course ${courses_materials[widget.list_of_courses[0][index]]
                              ['about']['name']} was pressed');
                            },
                            title: Text(widget.list_of_courses[0][index]),
                            subtitle: Text(courses_materials[widget.list_of_courses[0][index]]
                            ['about']['name']),
                            trailing: Icon(
                                Icons.download_outlined
                            ),
                          ),
                        ),
                      );
                    }),

                ListView.builder(
                    itemCount: widget.list_of_courses[1].length,
                    itemBuilder: (BuildContext context, int index){
                      return Card(
                        child: Container(
                          child: ListTile(
                            onTap: (){
                              print('course ${courses_materials[widget.list_of_courses[1][index]]
                              ['about']['name']} was pressed');
                            },
                            title: Text(widget.list_of_courses[1][index]),
                            subtitle: Text(courses_materials[widget.list_of_courses[1][index]]
                            ['about']['name']),
                            trailing: Icon(
                                Icons.download_outlined
                            ),
                          ),
                        ),
                      );
                    }),
              ],
            )),
      ),
    );
  }
}


//bringing scaffold it from the main to this side

class scafoldIt extends StatelessWidget {
  const scafoldIt({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: Courses(programYearCourses['computer']['1']),
      ),
    );
  }
}

