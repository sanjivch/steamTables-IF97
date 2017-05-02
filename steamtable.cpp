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


    temperature = ui->tempEdit->text();//ui->tempEdit->value();
    pressure = ui->presEdit->text();
    ui->enthalpyEdit->setText(QString::number(hmass_Tp(temperature.toDouble(), pressure.toDouble())/1000));
    ui->densityEdit->setText(QString::number(rhomass_Tp(temperature.toDouble(), pressure.toDouble())));

}



void steamTable::on_SIButton_clicked()
{
    ui->tempUnit->setText("deg K");
    ui->presUnit->setText("Pa");
}

void steamTable::on_MKSButton_clicked()
{
    ui->tempUnit->setText("deg C");
    ui->presUnit->setText("kg/m. s2");
}

void steamTable::on_EnglishButton_clicked()
{
    ui->tempUnit->setText("deg F");
    ui->presUnit->setText("psi");
}
