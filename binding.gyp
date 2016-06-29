{
	"targets": [
		{
			"includes": [
				"auto.gypi"
			],
			"sources": [
				"src/UiArea/UiArea.cc",
				"src/UiArea/DrawStrokeParams.cc",
				"src/UiArea/UiDrawContext.cc",
				"src/UiArea/UiDrawPath.cc",
				"src/UiArea/DrawBrush.cc",
				"src/SizeDouble.cc",
				"src/PointDouble.cc",
				"src/UiArea/DrawMatrix.cc",
				"src/UiArea/BrushGradientStop.cc",
				"src/UiArea/UiAreaDrawParams.cc",
				"src/UiArea/UiAreaKeyEvent.cc",
				"src/UiArea/UiAreaMouseEvent.cc",
				"src/UiArea/UiAreaHandler.cc",
				"src/UiGrid.cc",
				"src/UiForm.cc",
				"src/Size.cc",
				"src/Point.cc",
				"src/Color.cc",
				"src/UiColorButton.cc",
				"src/UiDialogs.cc",
				"src/UiMenu.cc",
				"src/UiCombobox.cc",
				"src/UiSlider.cc",
				"src/UiSpinbox.cc",
				"src/UiCheckbox.cc",
				"src/UiWindow.cc",
				"src/UiEntry.cc",
				"src/UiMultilineEntry.cc",
				"src/UiRadioButtons.cc",
				"src/UiEditableCombobox.cc",
				"src/UiGroup.cc",
				"src/UiTab.cc",
				"src/UiBox.cc",
				"src/UiDateTimePicker.cc",
				"src/UiSeparator.cc",
				"src/UiProgressBar.cc",
				"src/Ui.cc",
				"src/UiControl.cc",
				"src/UiLabel.cc",
				"src/UiButton.cc",
			],
			"conditions": [
				["OS!='mac'", {
					'ldflags': [
            					'-Wl,-rpath,<(module_root_dir)',
          				],
					"libraries": [
						"<(module_root_dir)/libui.so"
					]
				}]
			],
			"xcode_settings": {
				"OTHER_LDFLAGS": [
					"-L<(module_root_dir)",
					"-lui",
					"-rpath",
					"<(module_root_dir)"
				]
			}
		}
	],
	"includes": [
		"auto-top.gypi"
	]
}
