import 'package:flutter/material.dart';
// Package for enabling semantics
import 'package:flutter/rendering.dart';
// ---

import 'src/app.dart';

void main() {
  // Code for enabing semantics for the whole 
  // project (that generates a layer of pseudo elements on top)
  WidgetsFlutterBinding.ensureInitialized();
  SemanticsBinding.instance.ensureSemantics();
  // ---
  runApp(DashboardApp.mock());
}
