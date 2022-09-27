import 'package:flutter/material.dart';

import '../styles.dart';

class CommonFormField extends StatefulWidget {
  final date;
  final info;

  const CommonFormField({required this.date, required this.info});
  @override
  State<CommonFormField> createState() => _CommonFormFieldState(date, info);
}

class _CommonFormFieldState extends State<CommonFormField> {
  final dateText;
  final infoText;

  _CommonFormFieldState(this.dateText, this.infoText);
  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            dateText,
            style: subtitle3(mColor: Colors.white),
          ),
          Text(
            infoText,
            style: subtitle3(mColor: Colors.white),
          ),
          SizedBox(height: 1),
        ],
      ),
    );
  }
}
