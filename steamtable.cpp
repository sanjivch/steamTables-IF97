#include "steamtable.h"
#include "ui_steamtable.h"
#include "IF97.h"

using namespace std;
using namespace IF97;

steamTable::steamTable(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::steamTable)
{
    ui->setupUi(this);
}

steamTable::~steamTable()
{
    delete ui;
}

void steamTable::on_calcButton_clicked()
{
    QString temperature, pressure;

    //change pressure units
    temperature = ui->tempEdit->text();//ui->tempEdit->value();
    pressure = ui->presEdit->text();

    //if(temperature == "")



    if(ui->MKSButton->isChecked()){
        ui->enthalpyEdit->setText(QString::number(hmass_Tp(temperature.toDouble()+273.15, pressure.toDouble())/1000));
        ui->densityEdit->setText(QString::number(rhomass_Tp(temperature.toDouble()+273.15, pressure.toDouble())));
        ui->satLiqEnthalpyEdit->setText(QString::number(hliq_p(pressure.toDouble())/1000));
    }

    if(ui->SIButton->isChecked()){
        ui->enthalpyEdit->setText(QString::number(hmass_Tp(temperature.toDouble(), pressure.toDouble())/1000));
        ui->densityEdit->setText(QString::number(rhomass_Tp(temperature.toDouble(), pressure.toDouble())));
        ui->satLiqEnthalpyEdit->setText(QString::number(hliq_p(pressure.toDouble())/1000));
    }

    if(ui->EnglishButton->isChecked()){
        ui->enthalpyEdit->setText(QString::number(hmass_Tp(((temperature.toDouble()-32.0)/1.8) +273.15, pressure.toDouble())/1000));
        ui->densityEdit->setText(QString::number(rhomass_Tp(((temperature.toDouble()-32.0)/1.8)+273.15, pressure.toDouble())));
        ui->satLiqEnthalpyEdit->setText(QString::number(hliq_p(pressure.toDouble())/1000));
    }


}



void steamTable::on_SIButton_clicked()
{
    ui->tempUnit->setText("deg K");
    ui->presUnit->setText("Pa");
    ui->enthalpyUnit->setText("kJ/ kg");
    ui->densityUnit->setText("kg/ m3");
    ui->satLiqEnthalpyUnit->setText("kJ/ kg");
}

void steamTable::on_MKSButton_clicked()
{
    ui->tempUnit->setText("deg C");
    ui->presUnit->setText("kg/m. s2");
    ui->enthalpyUnit->setText("kcal/ kg");
    ui->densityUnit->setText("kg/ m3");
    ui->satLiqEnthalpyUnit->setText("kcal/ kg");
}

void steamTable::on_EnglishButton_clicked()
{
    ui->tempUnit->setText("deg F");
    ui->presUnit->setText("psi");
    ui->enthalpyUnit->setText("Btu/ lb");
    ui->densityUnit->setText("lb/ ft3");
    ui->satLiqEnthalpyUnit->setText("Btu/ lb");
}

void steamTable::on_resetButton_clicked()
{
    ui->tempEdit->setText("");
    ui->presEdit->setText("");

    ui->enthalpyEdit->setText("");
    ui->densityEdit->setText("");
    ui->satLiqEnthalpyEdit->setText("");
}
