import "package:flutter/material.dart";

class BottomNavigationBarState extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _BottomNavigationBarWidget();
  }
}

class _BottomNavigationBarWidget extends State<BottomNavigationBarState> {
  int _selectedIndex = 2;

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return BottomNavigationBar(

      currentIndex: _selectedIndex,
      unselectedFontSize: 12,
      selectedFontSize: 14,
      backgroundColor: Colors.blueAccent,
      selectedItemColor: Colors.white,
      unselectedItemColor: Colors.white.withOpacity(0.6),
      items: [
        BottomNavigationBarItem(
          icon: Icon(Icons.book),
          label: 'Schedule',
        ),
        BottomNavigationBarItem(
          icon: Icon(Icons.download_rounded),
          label: 'Downloads',
        ),
        BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
        BottomNavigationBarItem(
          icon: Icon(Icons.menu_book),
          label: 'Courses',
        ),
        BottomNavigationBarItem(icon: Icon(Icons.explore), label: 'Explore'),
      ],
      onTap: (index) {
        switch (index) {
          case 0:
            Navigator.pushNamed(context, "");
            break;
          case 1:
            Navigator.pushNamed(context, "");
            break;
          case 2:
            Navigator.pushNamed(context, "");
            break;
          case 3:
            Navigator.pushNamed(context, "");
            break;
          case 3:
            Navigator.pushNamed(context, "");
            break;
          default:
            Navigator.pushNamed(context, "");
        }
      },
    );
  }
}
