import 'package:flutter/material.dart';
import 'availablePrograms.dart';

class ChosenCourse extends StatefulWidget {
  List list_of_courses;
  String course_code = '';

  ChosenCourse(this.list_of_courses);

  @override
  _ChosenCourseState createState() => _ChosenCourseState();
}

class _ChosenCourseState extends State<ChosenCourse>
    with TickerProviderStateMixin {
//TabController had late before it
  TabController _controller;
  int _initialTabIndex = 0;
  //var _foundPrograms = [];

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _controller = TabController(length: 5, vsync: this);

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
      length: 5,
      child: Scaffold(
        body: NestedScrollView(
            headerSliverBuilder:
                (BuildContext context, bool innerBoxIsScrolled) {
              return <Widget>[
                SliverAppBar(
                  actions: [
                    //TODO: Quick search for course
                  ],
                  title: ListTile(
                    title: Text(
                      'course name',
                      style: TextStyle(fontSize: 35.0),
                    ),
                    subtitle: Text('Course code'),
                  ),
                  expandedHeight: 130.0,
                  pinned: true,
                  floating: true,
                  bottom: TabBar(
                    controller: _controller,
                    onTap: (_) {
                      print('tapped ${_} page');
                    },
                    tabs: [
                      Tab(
                        child: Text('Books'),
                      ),
                      Tab(
                        child: Text('Slides'),
                      ),
                      Tab(
                        child: Text('Prep'),
                      ),
                      Tab(child: Text('Videos')),
                      Tab(
                        child: Text('extras'),
                      )
                    ],
                  ),
                )
              ];
            },
            body: TabBarView(
              controller: _controller,
              children: [
                Container(
                  color: Colors.pinkAccent,
                ),
                Container(
                  color: Colors.transparent,
                ),
                Container(
                  color: Colors.tealAccent,
                ),
                Container(
                  color: Colors.transparent,
                ),
                Container(
                  color: Colors.deepOrangeAccent,
                )
              ],
            )),
      ),
    );
  }
}
